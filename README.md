[![Build Status](https://travis-ci.org/grape-gatorade/travelingcustomer.svg?branch=front-end-display)](https://travis-ci.org/grape-gatorade/travelingcustomer)


## Prerequisites

You'll need some package managers.

- `npm`
- `pip`

## Setup

For the backend:

```
virtualenv --no-site-packages .venv
. .venv/bin/activate
pip install -r requirements.txt
```

For the frontend:

If you don't have webpack, install it:

```
npm install -g webpack
```

Then, use `npm` to install the remaining JavaScript dependencies.

```
npm install
```

## Development

The entry point for the app is in `js/app.js`. The starter React component is `js/Hello.js`. Editing this file is a good place to start.

While developing on the frontend, run `webpack --watch` to keep re-compiling your JavaScript code.

Running `webpack` creates a file in `static/bundle.js`, which is the bundled version of your frontend code.

The "backend" here is a bare-bones Flask app. Look in `app.py` if you want to make edits to the backend.

To run the application, follow the steps in the next section.

## Running the app

If you're using a virtualenv, activate it.

```
. .venv/bin/activate
```

Then run the Flask app:

```
python app.py
```

