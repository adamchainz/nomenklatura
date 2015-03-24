from flask.ext.assets import Bundle

from nomenklatura.core import assets

deps_assets = Bundle(
    'vendor/jquery/dist/jquery.js',
    'vendor/bootstrap/js/collapse.js',
    'vendor/angular/angular.js',
    'vendor/angular-route/angular-route.js',
    'vendor/angular-loading-bar/build/loading-bar.js',
    'vendor/angular-bootstrap/ui-bootstrap-tpls.js',
    'vendor/ngUpload/ng-upload.js',
    filters='uglifyjs',
    output='assets/deps.js'
)

app_assets = Bundle(
    'js/app.js',
    'js/services/session.js',
    'js/directives/pagination.js',
    'js/directives/keybinding.js',
    'js/directives/authz.js',
    'js/controllers/app.js',
    'js/controllers/imports.js',
    'js/controllers/home.js',
    'js/controllers/docs.js',
    'js/controllers/review.js',
    'js/controllers/datasets.js',
    'js/controllers/entities.js',
    'js/controllers/profile.js',
    filters='uglifyjs',
    output='assets/app.js'
)

css_assets = Bundle(
    'vendor/font-awesome/less/font-awesome.less',
    # 'vendor/angular-loading-bar/build/loading-bar.css',
    'style/style.less',
    filters='less,cssrewrite',
    output='assets/style.css'
)

assets.register('deps', deps_assets)
assets.register('app', app_assets)
assets.register('css', css_assets)
