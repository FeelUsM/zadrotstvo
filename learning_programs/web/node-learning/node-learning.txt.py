Command Line Options
	for node command
TTY - modeule tty
	class tty.ReadStream - наследник net.Socket, - по умолчанию process.stdin - объект этого класса
	class tty.WriteStream - наследник net.Socket, - по умолчанию process.stdout, process.stderr - объект этого класса
Readline - module readline
	... для чтения строки за строкой
REPL - module repl
	... для создания интерактивной командной строки

Globals
	Javascript itself
		Standard
			Value properties
				Infinity
				NaN
				undefined
				null literal
			Function properties
				eval()
				isFinite()
				isNaN()
				parseFloat()
				parseInt()
				decodeURI()
				decodeURIComponent()
				encodeURI()
				encodeURIComponent()
			Fundamental objects
				Object
				Function
				Boolean
				Symbol
				Error
					EvalError
					InternalError
					RangeError
					ReferenceError
					SyntaxError
					TypeError
					URIError
			Numbers and dates
				Number
				Math
				Date
			Text processing
				String
				RegExp
			JSON
		Array
			[element0, element1, ..., elementN]
			new Array(element0, element1[, ...[, elementN]])
			new Array(arrayLength)
			
			Array.isArray()
			Array.from()
			Array.of()
			Array.prototype.length
			
			Array.prototype.fill()			(value[, start = 0[, end = this.length]])
			Array.prototype.splice()		(start, deleteCount[, item1[, item2[, ...]]])
			Array.prototype.pop()			()
			Array.prototype.push()			(element1, ..., elementN)
			Array.prototype.shift()			()
			Array.prototype.unshift()		([element1[, ...[, elementN]]])
			Array.prototype.sort()			([compareFunction])
			Array.prototype.reverse()		()
			Array.prototype.copyWithin()	(target[, start[, end]])
			Accessor methods
				Array.prototype.slice()
				Array.prototype.join()
				Array.prototype.concat()
				Array.prototype.indexOf()
				Array.prototype.lastIndexOf()
				Array.prototype.includes() 
				Array.prototype.toSource() 
				Array.prototype.toString()
				Array.prototype.toLocaleString()
			Iteration methods
				Array.prototype.forEach()
				Array.prototype.entries()
				Array.prototype.every()
				Array.prototype.some()
				Array.prototype.find()
				Array.prototype.findIndex()
				Array.prototype.keys()
				Array.prototype.filter()
				Array.prototype.map()
				Array.prototype.reduce()
				Array.prototype.reduceRight()
				Array.prototype.values()
				Array.prototype[@@iterator]()
		Raw data
			ArrayBuffer
				new ArrayBuffer(length)
				ArrayBuffer.isView(arg)
				ArrayBuffer.prototype.byteLength Read only
				ArrayBuffer.prototype.slice()
			DataView
				new DataView(buffer [, byteOffset [, byteLength]])
				DataView.prototype.buffer Read only
				DataView.prototype.byteLength Read only
				DataView.prototype.byteOffset Read only
				
				DataView.prototype.getInt8()
				DataView.prototype.getUint8()
				DataView.prototype.getInt16()
				DataView.prototype.getUint16()
				DataView.prototype.getInt32()
				DataView.prototype.getUint32()
				DataView.prototype.getFloat32()
				DataView.prototype.getFloat64()
				DataView.prototype.setInt8()
				DataView.prototype.setUint8()
				DataView.prototype.setInt16()
				DataView.prototype.setUint16()
				DataView.prototype.setInt32()
				DataView.prototype.setUint32()
				DataView.prototype.setFloat32()
				DataView.prototype.setFloat64()
			Int8Array
			Uint8Array
			Uint8ClampedArray
			Int16Array
			Uint16Array
			Int32Array
			Uint32Array
			Float32Array
			Float64Array
			TypedArray (one of Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array)
				new TypedArray(buffer [, byteOffset [, length]]);

				new TypedArray(length);
				new TypedArray(typedArray);
				new TypedArray(object); === TypedArray.from()
				TypedArray.BYTES_PER_ELEMENT
				TypedArray.length ===3
				TypedArray.name
				TypedArray.from()
				TypedArray.of()
				
				TypedArray.prototype.buffer Read only
				TypedArray.prototype.byteLength Read only
				TypedArray.prototype.byteOffset Read only
				TypedArray.prototype.length Read only
				
				TypedArray.prototype.subarray()
				TypedArray.prototype.set()

				TypedArray.prototype.fill()
				TypedArray.prototype.reverse()
				TypedArray.prototype.sort()
				TypedArray.prototype.copyWithin()
				Accessor methods
					TypedArray.prototype.slice()
					TypedArray.prototype.join()
					TypedArray.prototype.indexOf()
					TypedArray.prototype.lastIndexOf()
					TypedArray.prototype.includes() 
					TypedArray.prototype.toString()
					TypedArray.prototype.toLocaleString()
				Iteration methods
					TypedArray.prototype.forEach()
					TypedArray.prototype.entries()
					TypedArray.prototype.every()
					TypedArray.prototype.some()
					TypedArray.prototype.find()
					TypedArray.prototype.findIndex()
					TypedArray.prototype.keys()
					TypedArray.prototype.filter()
					TypedArray.prototype.map()
					TypedArray.prototype.reduce()
					TypedArray.prototype.reduceRight()
					TypedArray.prototype.values()
					TypedArray.prototype[@@iterator]()
		Control abstraction objects
			Promise
			Generator
			GeneratorFunction
		Keyed collections
			Map
			Set
			WeakMap
			WeakSet
		Reflection
			Reflect
			Proxy
		Internationalization
			Intl
			Intl.Collator
			Intl.DateTimeFormat
			Intl.NumberFormat
		Other
			arguments
	Class: Buffer
	__dirname	local to each module
	__filename	local to each module
	
	// var something - local to each module
	global
	module
	exports = module.exports
	require()
	require.cache
	require.extensions
	require.resolve()
	
	console
	process
	setImmediate(callback[, arg][, ...])
	setInterval(callback, delay[, arg][, ...])
	setTimeout(callback, delay[, arg][, ...])
	clearImmediate(immediateObject)
	clearInterval(intervalObject)
	clearTimeout(timeoutObject)

Modules - module module
	module.exports
	module.filename
	module.id
	module.loaded
	module.parent
	module.children - The module objects required by this one
	module.require(id) - как буд-то require() из указанного модуля
Utilities - module util
	util.debuglog(section)
	util.deprecate(function, string)
	util.format(format[, ...])
	util.inherits(constructor, superConstructor)
	util.inspect(object[, options])
		Customizing util.inspect colors
		Custom inspect() function on Objects
Console - global console !!!!!! + class Console
	global object console (by class Console)
	new Console(stdout[, stderr])
	class Console
		console.log([data][, ...])
		console.dir(obj[, options])
		console.trace(message[, ...])
		console.warn([data][, ...])
		console.error([data][, ...])
		console.info([data][, ...])
		console.assert(value[, message][, ...])
		console.time(label)
		console.timeEnd(label)
Assertion Testing - module assert
	assert(value[, message])
	assert.equal(actual, expected[, message])
	assert.notEqual(actual, expected[, message])
	assert.strictEqual(actual, expected[, message])
	assert.notStrictEqual(actual, expected[, message])
	assert.deepEqual(actual, expected[, message])
	assert.notDeepEqual(actual, expected[, message])
	assert.deepStrictEqual(actual, expected[, message])
	assert.notDeepStrictEqual(actual, expected[, message])
	assert.throws(block[, error][, message])
	assert.doesNotThrow(block[, error][, message])
	assert.ok(value[, message])
	assert.fail(actual, expected, message, operator)
	assert.ifError(value)
Errors = exception, но некоторые, которые вызывают падение node.js (assert вызывает abort()), не могут быть пойманы
	standard - от javascript
		<EvalError> : при вызове eval().
		<SyntaxError> : неправильный синатксис JavaScript.
		<RangeError> : за пределами дипозона
		<ReferenceError> : неопределенная переменная
		<TypeError> : аргументы неправильного типа
		<URIError> : неправильное использование глобальной функции обработки URI.
	system - от ОС
	user-specified - от пользователя
	assertion - от assert
	
	new Error(message)
	error.message - при наследовании надо устанавливать вручную
	error.prototype.name - при наследовании надо устанавливать вручную
	Error.captureStackTrace(targetObject[, constructorOpt]) - записывает стек в targetObject.stack
		constructorOpt - ссылка на функцию, которая и после которой в targetObject.stack ничего не попадет
	Error.stackTraceLimit
	error.stack
Debugger

Events - module events
	const EventEmitter = require('events');
	Class: EventEmitter
		Event: 'newListener'
		Event: 'removeListener'

		EventEmitter.defaultMaxListeners
		emitter.setMaxListeners(n) - при превышении этого числа в консоль идет warning
			0 - нет ограничения
		emitter.getMaxListeners()
		EventEmitter.listenerCount(emitter, eventName) - отсутствует в браузере
		emitter.listenerCount(eventName) - отсутствует в браузере
		emitter.listeners(eventName) - отсутствует в браузере

		emitter.addListener(eventName, listener)
		emitter.prependListener(eventName, listener)
		emitter.on(eventName, listener) - срабатывают в том порядке, в котором определены (в отличии от браузера)
		emitter.prependOnceListener(eventName, listener)
		emitter.once(eventName, listener)
		emitter.removeListener(eventName, listener)
		emitter.removeAllListeners([eventName])

		emitter.eventNames()
		emitter.emit(eventName[, arg1][, arg2][, ...])
			обработчик вызывается синхронно
			если событие было обработано - возвращает true, иначе false
Buffer - global class Buffer (as Uint8Array)
	...
Stream - module stream

OS
Path
File System
Process
... модуль heapdump 

Child Processes
Cluster

UDP/Datagram
URL
DNS
Domain
Net
HTTP
HTTPS

Punycode
Query Strings
String Decoder
Timers

V8
VM
C/C++ Addons

ZLIB
Crypto
TLS/SSL
