<aio.h>		
<arpa/inet.h>
<assert.h>
<complex.h>
<cpio.h>
<ctype.h>
<dirent.h>
<dlfcn.h>
<errno.h>
<fcntl.h>
<fenv.h>
<float.h>
<fmtmsg.h>
<fnmatch.h>
<ftw.h>
<glob.h>
<grp.h>
<iconv.h>
<inttypes.h>
<iso646.h>
<langinfo.h>
<libgen.h>
<limits.h>
<locale.h>
<math.h>
<monetary.h>
<mqueue.h>
<ndbm.h>
<net/if.h>
<netdb.h>
<netinet/in.h>
<netinet/tcp.h>
<nl_types.h>
<poll.h>
<pthread.h>
<pwd.h>
<regex.h>
<sched.h>
<search.h>
<semaphore.h>
<setjmp.h>
<signal.h>
<spawn.h>
<stdbool.h>
<stdint.h>
<stdlib.h>
<string.h>
<strings.h>
<stropts.h>
<sys/ipc.h>
<sys/mman.h>
<sys/msg.h>
<sys/resource.h>
<sys/select.h>
<sys/sem.h>
<sys/shm.h>
<sys/socket.h>
<sys/stat.h>
<sys/statvfs.h>
<sys/time.h>
<sys/times.h>
<sys/uio.h>
<sys/un.h>
<sys/utsname.h>
<sys/wait.h>
<syslog.h>
<tar.h>
<termios.h>
<tgmath.h>
<time.h>
<trace.h>
<ulimit.h>
<unistd.h>
<utime.h>
<utmpx.h>
<wchar.h>
<wctype.h>
<wordexp.h>




<stddef.h>	standard type definitions
<sys/types.h>	data types
<stdint.h>	integer types
<stdarg.h>	handle variable argument list
	handle variable argument list
		type va_arg  (va_list ap  , type);
		void va_copy (va_list dest, va_list src);
		void va_end  (va_list ap  );
		void va_start(va_list ap  , argN);
<stdio.h><stdarg.h>
	format output of a stdarg argument list
		int      vdprintf(int, const char *restrict, va_list); // CX
		int      vfprintf(FILE *restrict, const char *restrict, va_list);
		int      vprintf(const char *restrict, va_list);
		int      vsnprintf(char *restrict, size_t, const char *restrict, va_list);
		int      vsprintf(char *restrict, const char *restrict, va_list);
	format input of a stdarg argument list
		int      vfscanf(FILE *restrict, const char *restrict, va_list);
		int      vscanf(const char *restrict, va_list);
		int      vsscanf(const char *restrict, const char *restrict, va_list);
<stdio.h>	standard buffered input/output
	binary input
		size_t   fread(void *restrict, size_t, size_t, FILE *restrict);
	binary output
		size_t   fwrite(const void *restrict, size_t, size_t, FILE *restrict);

	get a byte from a stream
		int      fgetc(FILE *);
	get a byte from a stream
		int      getc(FILE *);
	get a byte from a stdin stream
		int      getchar(void);
	push byte back into input stream
		int      ungetc(int, FILE *);
	put a byte on a stream
		int      fputc(int, FILE *);
	put a byte on a stream
		int      putc(int, FILE *);
	put a byte on a stdout stream
		int      putchar(int);
	get a string from a stream
		char    *fgets(char *restrict, int, FILE *restrict);
	get a string from a stdin stream
		char    *gets(char *); // OB
	put a string on a stream
		int      fputs(const char *restrict, FILE *restrict);
	put a string on standard output
		int      puts(const char *);
	stdio with explicit client locking
		int      getc_unlocked(FILE *); // CX
		int      getchar_unlocked(void); // CX
		int      putc_unlocked(int, FILE *); // CX
		int      putchar_unlocked(int); // CX

	test end-of-file indicator on a stream
		int      feof(FILE *);
	print formatted output
		int      dprintf(int, const char *restrict, ...) // CX
		int      fprintf(FILE *restrict, const char *restrict, ...);
		int      printf(const char *restrict, ...);
		int      snprintf(char *restrict, size_t, const char *restrict, ...);
		int      sprintf(char *restrict, const char *restrict, ...);
	convert formatted input
		int      fscanf(FILE *restrict, const char *restrict, ...);
		int      scanf(const char *restrict, ...);
		int      sscanf(const char *restrict, const char *restrict, ...);
	read a delimited record from stream
		ssize_t  getdelim(char **restrict, size_t *restrict, int, FILE *restrict); // CX
		ssize_t  getline(char **restrict, size_t *restrict, FILE *restrict); // CX
	write error messages to standard error
		void     perror(const char *);

	open a memory buffer stream
		FILE    *fmemopen(void *restrict, size_t, const char *restrict); // CX
	open a stream
		FILE    *freopen(const char *restrict, const char *restrict, FILE *restrict);
	open a stream
		FILE    *fopen(const char *restrict, const char *restrict);
	close a stream
		int      fclose(FILE *);
	initiate pipe streams to or from a process
		FILE    *popen(const char *, const char *); // CX
	close a pipe stream to or from a process
		int      pclose(FILE *); // CX
	associate a stream with a file descriptor
		FILE    *fdopen(int, const char *); // CX
	map a stream pointer to a file descriptor
		int      fileno(FILE *); // CX
	flush a stream
		int      fflush(FILE *);
	assign buffering to a stream
		void     setbuf(FILE *restrict, char *restrict);
	assign buffering to a stream
		int      setvbuf(FILE *restrict, char *restrict, int, size_t);

	get current file position information
		int      fgetpos(FILE *restrict, fpos_t *restrict);
	set current file position
		int      fsetpos(FILE *, const fpos_t *);
	reposition a file-position indicator in a stream
		int      fseek(FILE *, long, int);
		int      fseeko(FILE *, off_t, int); // CX
	reset the file position indicator in a stream
		void     rewind(FILE *);
	return a file offset in a stream
		long     ftell(FILE *);
		off_t    ftello(FILE *); // CX
	clear indicators on a stream
		void     clearerr(FILE *);
	test error indicator on a stream
		int      ferror(FILE *);

	generate a pathname for the controlling terminal
		char    *ctermid(char *); // CX
	stdio locking functions
		void     flockfile(FILE *); // CX
		int      ftrylockfile(FILE *); // CX
		void     funlockfile(FILE *); // CX
	remove a file
		int      remove(const char *);
	create a name for a temporary file
		char    *tempnam(const char *, const char *); // OB XSI
	create a name for a temporary file
		char    *tmpnam(char *); // OB
	create a temporary file
		FILE    *tmpfile(void);
<locale.h>	category macros
	return locale-specific information
		struct lconv *localeconv(void);
	set program locale
		char         *setlocale(int, const char *);
	use locale in current thread
		locale_t      uselocale (locale_t);	// CX
	create or modify a locale object
		locale_t      newlocale(int, const char *, locale_t);	// CX
	duplicate a locale object
		locale_t      duplocale(locale_t);	// CX
	free resources allocated for a locale object
		void          freelocale(locale_t);	// CX







<stdio.h><wchar.h>
	open a dynamic memory buffer stream
		FILE    *open_memstream(char **, size_t *); // CX
		FILE 	*open_wmemstream(wchar_t **bufp, size_t *sizep); // CX
<stdio.h><fcntl.h>
	rename file
		int      rename(const char *, const char *);
		int      renameat(int, const char *, int, const char *); // CX
