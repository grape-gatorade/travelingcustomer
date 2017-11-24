var webpack = require('webpack');

module.exports = {  
  entry: [
    "./js/app.js"
  ],
  output: {
    path: __dirname + '/static',
    filename: "bundle.js"
  },
  module: {
    preLoaders: [
      {
        test: /\.js?$/,
        loader: 'eslint-loader',
        options: {
          fix: true,
        }
      }
    ],
    loaders: [
      {
        test: /\.js?$/,
        loader: 'babel-loader',
        cacheDirectory: true,
        query: {
          plugins: ['transform-decorators-legacy'],
          presets: ['es2015', 'stage-0', 'react']
        },
        exclude: /node_modules/
      },
      {
        test: /\.css$/,
        loader: 'style!css!',
      },
    ]
  },
  plugins: [
  ],
};
