// See http://brunch.io for documentation.
exports.files = {
  javascripts: {
    joinTo: {
      'app.js': /^app/,
      'vendor.js': /^node_modules/
    }
  },
  stylesheets: {
    joinTo: {
      'app.css': /^app/
    }
  }
};

module.exports.plugins = {
  babel: { presets: ['env', 'react'] },
  sass: {
    options: {
      includePaths: [ 'app/', 'node_modules/bootstrap-sass/assets/stylesheets/' ],
      precision: 8
    }
  }
};
