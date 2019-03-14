/* Implementation of NIST's Secure Hash Algorithm (FIPS 180-1)
 *
 * Adapted from an implementation by Jim Gillogly of 5 Jul 94
 *
 * LITTLE_ENDIAN mods from Peter Gutmann's implementation
 *
 * SHA-1 is a technical revision of the original SHA (FIPS 180)
 * incorporating a fix for a weakness in SHA discovered by the
 * National Security Agency.
*/


#include <stdio.h>
#include <memory.h>
#include <string.h>
#include "pgp.h"
#include "mpilib.h"
#include "sha1.h"
#include "fileio.h"
#include "language.h"
#ifdef MACPGP
#include "Macutil3.h"
#endif

int mdalg_flag = 0;
#define SHA1_DEBUG

#ifdef SHA1_DEBUG
static char current_dbg_file[12] = "shadbg";
static FILE *SHA1_f = NULL;
#endif

void SHA1Init(struct SHA1Context *context)
{
	int i;

	context->h0 = 0x67452301L;
    context->h1 = 0xefcdab89L;
    context->h2 = 0x98badcfeL;
    context->h3 = 0x10325476L;
    context->h4 = 0xc3d2e1f0L;
	context->hi_length = 0;
	context->lo_length = 0;
	context->inbytes = 0;
	context->padded = FALSE;
	for (i=0; i<80; i++)
		context->in.W[i] = 0L;
#ifdef SHA1_DEBUG
	if (file_exists("shadbg")) {
		int i;
		for (i=0; i<100; i++) {
			current_dbg_file[6] = (i>9 ? '0' + i/10 : '0' + i);
			current_dbg_file[7] = (i>9 ? '0' + (i%10) : 0);
			current_dbg_file[8] = 0;
			if (!file_exists(current_dbg_file))
				break;
		}
		if (i<100)	
			SHA1_f = fopen(current_dbg_file,"wb");
	}
#endif
}

#ifndef HIGHFIRST   /* Imported from Peter Gutmann's implementation */

/* When run on a little-endian CPU we need to perform byte reversal on an
   array of longwords.  It is possible to make the code endianness-
   independant by fiddling around with data at the byte level, but this
   makes for very slow code, so we rely on the user to sort out endianness
   at compile time */

static void byteReverse( uint32 *buffer, int byteCount )
    {
    uint32 value;
    int count;

    byteCount /= sizeof( uint32 );
    for( count = 0; count < byteCount; count++ )
	{
	value = ( buffer[ count ] << 16 ) | ( buffer[ count ] >> 16 );
	buffer[ count ] = ( ( value & 0xFF00FF00L ) >> 8 ) | ( ( value & 0x00FF00FFL ) << 8 );
	}
    }
#endif /* HIGHFIRST */

#define f0(x,y,z) (z ^ (x & (y ^ z)))           /* Magic functions */
#define f1(x,y,z) (x ^ y ^ z)
#define f2(x,y,z) ((x & y) | (z & (x | y)))
#define f3(x,y,z) (x ^ y ^ z)

#define K0 0x5a827999                           /* Magic constants */
#define K1 0x6ed9eba1
#define K2 0x8f1bbcdc
#define K3 0xca62c1d6

#define S(n, X) ((X << n) | (X >> (32 - n)))    /* Barrel roll */

#define r0(f, K) \
    temp = S(5, A) + f(B, C, D) + E + *p0++ + K; \
    E = D;  \
    D = C;  \
    C = S(30, B); \
    B = A;  \
    A = temp

#ifdef VERSION_0
#define r1(f, K) \
    temp = S(5, A) + f(B, C, D) + E + \
	   (*p0++ = *p1++ ^ *p2++ ^ *p3++ ^ *p4++) + K; \
    E = D;  \
    D = C;  \
    C = S(30, B); \
    B = A;  \
    A = temp
#else                   /* Version 1: Summer '94 update */
#define r1(f, K) \
    temp = *p1++ ^ *p2++ ^ *p3++ ^ *p4++; \
    temp = S(5, A) + f(B, C, D) + E + (*p0++ = S(1,temp)) + K; \
    E = D;  \
    D = C;  \
    C = S(30, B); \
    B = A;  \
    A = temp
#endif

/* This is the guts of the SHA1 calculation.  If we can get 64 bytes into
   the holding context->in buffer, we go ahead and process these bytes,
   adding them to the accumulated message digest. If not, and finalize is
   false, we just store however many bytes we can get for future use.
   If finalize is true, we pad this block to 64 bytes and try to fit in the
   accumulated bit length of the message (which we can do only if the
   original block < 56 bytes). We return TRUE if we need to add one more
   block to fit in the bit length. (Returned value is only significant if
   finalize is true.) The pointer to the input buffer is advanced and its
   length is updated in every case. */

int SHA1Update0(struct SHA1Context *context, unsigned char const **buf,
	       unsigned *len, int finalize)
{
    int i, nread, nbits;
    char *s;
    register uint32 *p0, *p1, *p2, *p3, *p4;
    uint32 A, B, C, D, E, temp;

	if (*len < 64 - context->inbytes) {
		if (*len) {
			memcpy(context->in.B + context->inbytes, *buf, *len);
			*buf += *len;
			context->inbytes += *len;
			*len = 0;
		}
		if (!finalize)
			return TRUE;
		nread = context->inbytes;
		context->inbytes = 0;
		nbits = nread << 3;               /* Length: bits */
		if ((context->lo_length += nbits) < nbits)
			context->hi_length++;              /* 64-bit integer */

		if ( ! context->padded)  /* Append a single bit */
		{
			context->in.B[nread++] = 0x80; /* Using up next byte */
			context->padded = TRUE;       /* Single bit once */
		}
		for (i = nread; i < 64; i++) /* Pad with nulls */
			context->in.B[i] = 0;
		if (nread <= 56)   /* Room for length in this block */
		{
			context->in.W[14] = context->hi_length;
			context->in.W[15] = context->lo_length;
#ifndef HIGHFIRST
	      byteReverse(context->in.W, 56 );
#endif /* HIGHFIRST */
		}
#ifndef HIGHFIRST
	   else byteReverse(context->in.W, 64 );
#endif /* HIGHFIRST */
	} else {
		memcpy(context->in.B + context->inbytes, *buf, 64 - context->inbytes);
		*buf += 64 - context->inbytes;
		*len -= 64 - context->inbytes;
		context->inbytes = 0;
		if ((context->lo_length += 512) < 512)
			context->hi_length++;    /* 64-bit integer */
#ifndef HIGHFIRST
	   byteReverse(context->in.W, 64 );
#endif /* HIGHFIRST */
	}
	p0 = context->in.W;
	A = context->h0; B = context->h1;
	C = context->h2; D = context->h3;
	E = context->h4;

	r0(f0,K0); r0(f0,K0); r0(f0,K0); r0(f0,K0); r0(f0,K0);
	r0(f0,K0); r0(f0,K0); r0(f0,K0); r0(f0,K0); r0(f0,K0);
	r0(f0,K0); r0(f0,K0); r0(f0,K0); r0(f0,K0); r0(f0,K0);
	r0(f0,K0);

	p1 = &context->in.W[13]; p2 = &context->in.W[8];
	p3 = &context->in.W[2]; p4 = &context->in.W[0];

		   r1(f0,K0); r1(f0,K0); r1(f0,K0); r1(f0,K0);
	r1(f1,K1); r1(f1,K1); r1(f1,K1); r1(f1,K1); r1(f1,K1);
	r1(f1,K1); r1(f1,K1); r1(f1,K1); r1(f1,K1); r1(f1,K1);
	r1(f1,K1); r1(f1,K1); r1(f1,K1); r1(f1,K1); r1(f1,K1);
	r1(f1,K1); r1(f1,K1); r1(f1,K1); r1(f1,K1); r1(f1,K1);
	r1(f2,K2); r1(f2,K2); r1(f2,K2); r1(f2,K2); r1(f2,K2);
	r1(f2,K2); r1(f2,K2); r1(f2,K2); r1(f2,K2); r1(f2,K2);
	r1(f2,K2); r1(f2,K2); r1(f2,K2); r1(f2,K2); r1(f2,K2);
	r1(f2,K2); r1(f2,K2); r1(f2,K2); r1(f2,K2); r1(f2,K2);
	r1(f3,K3); r1(f3,K3); r1(f3,K3); r1(f3,K3); r1(f3,K3);
	r1(f3,K3); r1(f3,K3); r1(f3,K3); r1(f3,K3); r1(f3,K3);
	r1(f3,K3); r1(f3,K3); r1(f3,K3); r1(f3,K3); r1(f3,K3);
	r1(f3,K3); r1(f3,K3); r1(f3,K3); r1(f3,K3); r1(f3,K3);

	context->h0 += A; context->h1 += B;
	context->h2 += C; context->h3 += D;
	context->h4 += E;
	
	return nread > 56;
}

/* Add one buffer's worth of bytes to the SHA1 calculation. If the number of
   bytes in the buffer is not a multiple of 64, hold the bytes in the last
   partial block in the context->in holding area for the next time this
   routine is called. */
void SHA1Update(struct SHA1Context *context, unsigned char const *buf,
	       unsigned len)
{
	unsigned len2 = len;
	unsigned char const *buf2 = buf;
	while (len2)
		SHA1Update0(context, &buf2, &len2, FALSE);
#ifdef SHA1_DEBUG
	if (SHA1_f)
		fwrite(buf, 1, len, SHA1_f);
#endif
}

/* Finish off the SHA1 calculation by adding in the left over bytes in
   context->in with padding and with the total bit length of the message.
   May have to call SHA1Update0() twice, if there isn't enough room to
   process the bit length the first time around. */
void SHA1Final(unsigned char digest[20], struct SHA1Context *context)
{
	unsigned len = 0L;
	uint32 *p = (uint32 *)digest;
	while (SHA1Update0(context, (void *)NULL, &len, TRUE));
	p[0] = context->h0; p[1] = context->h1; p[2] = context->h2;
	p[3] = context->h3; p[4] = context->h4;
#ifdef SHA1_DEBUG
	if (SHA1_f) {
		char output_file[16];
		FILE *g;
		fclose(SHA1_f);
		strcpy(output_file, current_dbg_file);
		strcat(output_file, ".sha");
		if (g = fopen(output_file,"w")) {
 			fprintf(g,"%08lx %08lx %08lx %08lx %08lx\n",
		    	p[0], p[1], p[2], p[3], p[4]);
		    fclose(g);
		}
		SHA1_f = NULL;
	}
#endif
#ifndef HIGHFIRST
    byteReverse((uint32 *)digest, 20);
#endif
    memset(context, 0, sizeof(context));	/* In case it's sensitive */
}

/* Note - the routines in this module, except for SHA1_addbuffer,
 * do not "finish" the SHA1 calculation.  SHA1_addbuffer finishes the
 * calculation in each case, usually to append the timestamp and class info.
 */

/* Computes the message digest for a file from current position for
   longcount bytes.
   Uses the SHA-1 Message Digest Algorithm */

int SHA1file0_len(struct SHA1Context *shContext, FILE * f, word32 longcount)
{
    int bytecount;
    unsigned char buffer[1024];

    SHA1Init(shContext);
    /* Process 1024 bytes at a time... */
    do {
	if (longcount < (word32) 1024)
	    bytecount = (int) longcount;
	else
	    bytecount = 1024;
	bytecount = fread(buffer, 1, bytecount, f);
	if (bytecount > 0) {
	    SHA1Update(shContext, buffer, bytecount);
	    longcount -= bytecount;
#ifdef MACPGP
		mac_poll_for_break();
#endif
	}
	/* if text block was short, exit loop */
    } while (bytecount == 1024);
    return 0;
}				/* SHA1file0_len */


/* Computes the message digest for a file from current position to EOF.
   Uses the SHA1 Message Digest Algorithm */

static int SHA1file0(struct SHA1Context *shContext, FILE * inFile)
{
    int bytes;
    unsigned char buffer[1024];

    SHA1Init(shContext);
    while ((bytes = fread(buffer, 1, 1024, inFile)) != 0)
#ifdef MACPGP
		{
		mac_poll_for_break();
		SHA1Update(shContext,buffer,bytes);
		}
#else
	SHA1Update(shContext, buffer, bytes);
#endif
    return 0;
}

/* Computes the message digest for a specified file */

int SHA1file(struct SHA1Context *shContext, char *filename)
{
    FILE *inFile;
    inFile = fopen(filename, FOPRBIN);

    if (inFile == NULL) {
	fprintf(pgpout, LANG("\n\007Can't open file '%s'\n"), filename);
	return -1;
    }
    SHA1file0(shContext, inFile);
    fclose(inFile);
    return 0;
}

/* Add a buffer's worth of data to the SHA1 computation.  If a digest
 * pointer is supplied, complete the computation and write the digest.
 */
void SHA1_addbuffer(struct SHA1Context *shContext, byte * buf, int buflen,
		  byte digest[20])
{
    SHA1Update(shContext, buf, buflen);
    if (digest) {
	SHA1Final(digest, shContext);
	burn(*shContext);	/* Paranoia */
    }
}

/* End SHA1 routines */
