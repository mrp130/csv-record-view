import sublime
import sublime_plugin
import re

class CsvrecordviewCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		r = re.compile(r'''\s*([^,"']*?|"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')\s*(?:,|$)''', re.UNICODE)
		for cursor in self.view.sel():
			for line in self.view.lines(cursor):
				text = self.view.substr(line)
				text = text.strip()
				
				arr = r.findall(text)
				output = '\n'.join(arr)
				new_view = sublime.active_window().new_file()
				new_view.insert(edit, 0, output)
