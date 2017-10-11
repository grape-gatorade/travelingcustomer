// See http://brunch.io for documentation.
exports.files = {
  javascripts: {joinTo: 'app.js'},
  stylesheets: {joinTo: 'app.css'}
};

module.exports.plugins = {
  babel: {
    presets: ['env', 'react'],
    ignore: [ /^node_modules/ ]
  }
};
