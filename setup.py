import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lucidsonicdreams", 
    version="0.42",
    author="The AI Repair Guy",
    author_email="anon@gmail.com",
    description="Syncs GAN-generated visuals to music",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pollinations/lucid-sonic-dreams",
    download_url="https://github.com/pollinations/lucid-sonic-dreams/archive/refs/tags/v_04.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['resampy==0.3.1',
                      'librosa==0.7.2',
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
