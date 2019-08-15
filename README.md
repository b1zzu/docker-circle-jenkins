# Images

This is a collection of images for that could be used in CI/CD pipelines. Each Dockerfile is just a piece of what it could became the final image and they can be composed together using the build.py script.

Fore example this command will create an image based on fedora, with openjdk and gradle

```bash
./build.py fedora:31 openjdk8 gradle:5.6
```

the fedora version can be easily swapped

```bash
./build.py fedora:29 openjdk8 gradle:5.6
```

> Not all imaginable combination will be possible but in this way it will be easier to reuse different images.
