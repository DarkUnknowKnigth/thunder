(function() {
    'use strict';
    var snackbarContainer = document.querySelector('#demo-toast-example');
    var showToastButton = document.querySelector('#demo-show-toast');
    showToastButton.addEventListener('click', function() {
        'use strict';
        var data = {
            message: "This app was created with Flask, Jinja2 and Thunder"
        };
        snackbarContainer.MaterialSnackbar.showSnackbar(data);
    });
}());