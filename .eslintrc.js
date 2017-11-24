module.exports = {
    "extends": "airbnb",
     "env": {
        "node": true,
        "es6": true
     },
     "rules": {
        "react/jsx-filename-extension": [1, { "extensions": [".js", ".jsx"] }],
        "react/forbid-prop-types": 0,
        "react/prefer-stateless-function": 0,
        "react/prop-types": 0,
        "linebreak-style": 0,
        "react/no-render-return-value": 0,
        "no-underscore-dangle": 0,
     },
     "parser": "babel-eslint"
   };