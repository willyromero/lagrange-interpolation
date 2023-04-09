# **Lagrange Interpolation.** :eyes

This is a basic solution for solve Lagrange polynomials.

## **Install requirements.**

Open terminal and type

```shell
virtualenv .venv
```

Active virtual environment

```shell
.venv\Scripts\activate
```

Install requirements

```shell
pip install -r requirements.txt
```

## 1. **How to use.**

---

Add more elements to `data.json` more elements with this structure:

```json
  {
    "data": {
      "xi": [value1, value2, valueN],
      "fi": [value1, value2, valueN]
    }
  }
```

When you use code for resolve `data.json` file changes and add the **results** like this:

```json
    "results": {
      "fn(x)": "some polynomial",
      "simplified_fn(x)": "some simplified polynomial"
    }
```
