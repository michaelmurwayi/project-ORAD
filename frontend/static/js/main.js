(function ($) {
    "use strict";

    // Function to close opened dropdowns
    function closeDropdowns() {
        var sidebar = $('#sidebar');
        var dropdowns = sidebar.find('.left-menu-dropdown');

        // Hide dropdowns
        dropdowns.css({
            'opacity': 0,
            'left': '0'
        });
    }

    /*----------------------------
     jQuery MeanMenu
    ------------------------------ */
    jQuery('nav#dropdown').meanmenu();

    /*----------------------------
     jQuery myTab
    ------------------------------ */
    $('#myTab a').on('click', function (e) {
        e.preventDefault();
        $(this).tab('show');
    });

    $('#myTab3 a').on('click', function (e) {
        e.preventDefault();
        $(this).tab('show');
    });

    $('#myTab4 a').on('click', function (e) {
        e.preventDefault();
        $(this).tab('show');
    });

    $('#myTabedu1 a').on('click', function (e) {
        e.preventDefault();
        $(this).tab('show');
    });

    $('#single-product-tab a').on('click', function (e) {
        e.preventDefault();
        $(this).tab('show');
    });

    $('[data-toggle="tooltip"]').tooltip();

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        // Close opened dropdowns when sidebar is closed
        if (!$('#sidebar').hasClass('active')) {
            closeDropdowns();
        }
    });

    // Collapse ibox function
    $('#sidebar ul li').on('click', function () {
        var button = $(this).find('i.fa.indicator-mn');
        button.toggleClass('fa-plus').toggleClass('fa-minus');
    });

    /*-----------------------------
     Menu Stick
    ---------------------------------*/
    $(".sicker-menu").sticky({topSpacing:0});

    $('#sidebarCollapse').on('click', function () {
        $("body").toggleClass("mini-navbar");
        SmoothlyMenu();
        // Close opened dropdowns when sidebar is closed
        if ($("body").hasClass("mini-navbar")) {
            closeDropdowns();
        }
    });

    $(document).on('click', '.header-right-menu .dropdown-menu', function (e) {
        e.stopPropagation();
    });

    /*----------------------------
     wow js active
    ------------------------------ */
    new WOW().init();

    /*----------------------------
     owl active
    ------------------------------ */
    $("#owl-demo").owlCarousel({
        autoPlay: false,
        slideSpeed:2000,
        pagination:false,
        navigation:true,
        items : 4,
        navigationText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"],
        itemsDesktop : [1199,4],
        itemsDesktopSmall : [980,3],
        itemsTablet: [768,2],
        itemsMobile : [479,1],
    });

    /*--------------------------
     scrollUp
    ---------------------------- */
    $.scrollUp({
        scrollText: '<i class="fa fa-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });

    /*--------------------------
     left-side nav
    ---------------------------- */
})(jQuery);

// Example AJAX login request
const loginForm = document.getElementById('loginForm');
loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(loginForm);
    fetch('/login/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Handle response data
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
