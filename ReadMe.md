Steps to follow when deploying Machine Learning Model
1 - Build Machine Learning Model - Train - Tune - Test -> Production Ready
2 - Build Machine Learning REST API (Flask/ FastAPI) - We are using FastAPI
3 - Build Frontend App/UI using StreamLit/Other framework - We are using Streamlit
4 - Run local FastAPI & expose ML API end points
5 - Test & debug ML API exposed by development server
6 - Run Streamlit frontend App to access the ML API exposed by local development server
7 - Write Dockerfile to containerize ML API & Environment
8 - Build Docker Images
9 - Run Docker Images to launch a container
10 - Test & debug ML API exposed by docker container
11 - Run Streamlit frontend App to access the ML API endpoint exposed by Docker container
12 - Push docker image to registry (Docker hub, AWS/Azure/Google) container registry)

## Picker or Joblib
What is Pickle
pickle is a module built-in in Python which allows for Python object serialization. “Pickling” is the process in which a Python object is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream is converted back into Python objects.

The name comes from the verb “to pickle”, which means “preserving vegetables for later use”: in the same way, Python objects are serialized into files for later use.

What is Joblib
joblib is a set of tools to provide lightweight pipelining in Python. It focuses on disk-caching, memoization, and parallel computing. The library is optimized to be fast and robust on large data in particular and has specific optimizations for NumPy arrays.

Since pipelining is used to efficiently manage a large amount of data, joblib contains a replacement for pickle to work efficiently on large data.