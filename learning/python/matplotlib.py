import matplotlib.pyplot as plt

################## figure
fig = plt.figure()  						# get figure
fig.suptitle('No axes on this figure')

fig, ax_lst = plt.subplots(2, 2)  			# set cols/rows of axes and get figure and axes

################## axes
axes.set_xlim(...)
axes.set_ylim(...)

axes.set_title(...)
axes.set_xlabel(...)
axes.set_ylabel(...)

axes.plot(x,y,params)
	params:
		marker:'x'|'o'

################## axis
axis = axes.get_xaxis() # get axis

axis.get_major_formatter()
axis.get_major_locator()

################## пример использования pyplot
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear') # первый вызов  автоматически создаст необходимые figure and axes
plt.plot(x, x**2, label='quadratic') # использует текущий axes
plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

plt.show()

################### пример использования ОО интерфейса

x = np.arange(0, 10, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()

###################  module matplotlib
import matplotlib #as mpl

matplotlib.use(arg, warn=False, force=True) # установить backend
matplotlib.get_backend()                    

class matplotlib.RcParams(*args, **kwargs)  # класс для хранения параметров
	copy()
	find_all(pattern)
	validate                                     # словарь с функциями валидации
matplotlib.rcParams                         # текущие параметры

matplotlib.rc_context(rc=None, fname=None)  # with rc_context(...) строим график

matplotlib.rc(group, **kwargs)              # устанавливает rc параметры
matplotlib.rc_file(fname)                   # устанавливает параметры из файла
matplotlib.rcdefaults()                     # устанавливает параметры по умолчанию
matplotlib.rc_file_defaults()               # устанавливает параметры из rc файла по умолчанию

matplotlib.rc_params(fail_on_error=False)   # возвращает параметры из rc файла по умолчанию
matplotlib.rc_params_from_file(fname, fail_on_error=False, use_default_template=True) # 
matplotlib.matplotlib_fname()               # путь к файлу с конфигами

matplotlib.interactive(b)                   # устанавливает интерактивность
matplotlib.is_interactive()                 # проверяет интерактивность

####################  module style
import matplotlib.style
matplotlib.style.context(style, after_reset=False)
matplotlib.style.reload_library()
matplotlib.style.use(style)
matplotlib.style.library                    # словарь доступных стилей
matplotlib.style.available                  # список доступных стилей


##################### modeule rcsetup
import matplotlib.rcsetup
# дефолтные параметры и функции их валидации
