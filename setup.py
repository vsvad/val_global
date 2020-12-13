import setuptools

long_description = '''
<h1>Val_global</h1>
<p>Create global variables. Usage:</p>
<pre><code>
import val_global<br>
n=val_global.Value()<br>
print(n.get()) # None<br>
n.set(4)<br>
print(n.get()) # 4<br>
n.clear()<br>
print(n.get()) # None<br>
@val_global.result_to_val(1,2,3)<br>
def v(a,b,c):<br>
	return a*b*c<br>
print(v.get()) # 6<br>
v.set(5)<br>
print(v.get()) # 5</code></pre>
'''

setuptools.setup(
    name="val_global", # Replace with your own username
    version="0.0.1",
    author='Vadim Simakin',
    author_email="sima.vad@gmail.com",
    description="Global variables without \"global\" operator",
    long_description=long_description,
    long_description_content_type="text/html",
    url="https://github.com/vsvad/var_global",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)