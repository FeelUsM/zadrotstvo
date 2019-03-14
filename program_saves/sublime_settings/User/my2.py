import sublime
import sublime_plugin

prnt = lambda x: window.run_command('my',{'a':x})

class My2(sublime_plugin.TextCommand):
	def run(self, edit):
		print('Hello, World!',args['a'])
		#sublime.message_dialog('Hello')
		sublime.status_message('Hello')
		#self.view.insert(edit, 0, "Hello, World!")

		window = sublime.active_window()
		nnn=window.create_output_panel('nnn')
		window.run_command('show_panel',dict(panel='nnn'))
		#sublime.active_window().run_command('show_panel',dict(panel='find_in_files'))
