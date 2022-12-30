import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lucidsonicdreams", 
    version="0.01",
    author="BigZaddy",
    author_email="@gmail.com",
    description="Syncs GAN-generated visuals to music",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/takerdao2/lucid-sonic-dreams",
    download_url="https://github.com/takertao2/lucid-sonic-dreams/lucid-sonic-dreams.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['resampy==0.3.1',
                      'librosa==0.6.0',
                      'numba==0.37.0',
                      'numpy==1.17.3',
                      'tensorflow==1.15',
                      'moviepy',
                      'Pillow',
                      'tqdm',
                      'scipy==1.4.1',
                      'scikit-image',
                      'pygit2',
                      'gdown', 
                      'mega.py',
                      'requests',
                      'pandas',
                      'SoundFile']
)
