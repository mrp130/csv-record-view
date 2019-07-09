import sublime
import sublime_plugin
import re

class CsvrecordviewCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		settings = sublime.load_settings("csv_record_view.sublime-settings")
		delimiter = settings.get('csvrecordview_delimiter')
		if delimiter is None:
			delimiter = self.view.settings().get('csvrecordview_delimiter')
		if delimiter is None:
			delimiter = ','

		regex_string = r'''\s*([^${delimiter}"']*?|"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')\s*(?:${delimiter}|$)'''
		regex_string = regex_string.replace(r'${delimiter}', delimiter)

		r = re.compile(regex_string, re.UNICODE)
		for cursor in self.view.sel():
			for line in self.view.lines(cursor):
				text = self.view.substr(line)
				text = text.strip()
				
				arr = r.findall(text)
				output = '\n'.join(arr)
				new_view = self.view.window().new_file()
				new_view.insert(edit, 0, output)
