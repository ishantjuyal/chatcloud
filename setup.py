from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='chatclouds',
  version='0.0.5',
  description='Allows you to make wordclouds for your Whatsapp Chats',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/ishantjuyal/chatcloud',  
  author='Ishant Juyal',
  author_email='ishantnit@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='wordcloud', 
  packages=find_packages(),
  install_requires=['wordcloud', 'matplotlib', 'pandas', 'contractions'] 
)