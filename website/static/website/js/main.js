window.jQuery(document).ready(function($) {

    'use strict';

    // Script for Header Background - Height 100% //
    if ($(document).width() >= 769) {
        $(window).on("resize", function() {
            if ($(window).width() < 769) {
                $('.header-content').height("auto"); // Mobile version size "auto"
            } else {
                var height = $(window).height(); //Get the height of the browser window
                $('.header-content').height(height - 150); //Resize the videocontainer div, with a size of 64 - page height.
            }
        }).resize();
    } else {}
    // End Script for Header Background - Height 100% //


    // jQuery smooth scrolling //
    $('a[href*="#"]').on('click', function(e) {
        e.preventDefault();
        var target = this.hash;
        var $target = $(target);
        $('html, body').stop().animate({
            'scrollTop': $target.offset().top
        }, 900, 'swing', function() {
            window.location.hash = target;
        });
    });
    // End jQuery smooth scrolling //

    jQuery(document).ready(function($) {
        // Scroll to top button
        // browser window scroll (in pixels) after which the "back to top" link is shown
        var offset = 300,
            //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
            offset_opacity = 1200,
            //duration of the top scrolling animation (in ms)
            scroll_top_duration = 700,
            //grab the "back to top" link
            $back_to_top = $('.cd-top');

        //hide or show the "back to top" link
        $(window).scroll(function() {
            ($(this).scrollTop() > offset) ? $back_to_top.addClass('cd-is-visible'): $back_to_top.removeClass('cd-is-visible cd-fade-out');
            if ($(this).scrollTop() > offset_opacity) {
                $back_to_top.addClass('cd-fade-out');
            }
        });

        //smooth scroll to top
        $back_to_top.on('click', function(event) {
            event.preventDefault();
            $('body,html').animate({
                scrollTop: 0,
            }, scroll_top_duration);
        });
        // End Scroll to top

        // Mobile Menu Show Hide Submenu
        $('#header .navbar-default li.subnav ul').after('<div class="nav__expand"><i class="fas fa-chevron-down"></i></div>');
        $("#header .navbar-default li.subnav .nav__expand").on('click', function() {
            $(this).prev("ul").slideToggle("slow");
        });
    });


    // Navigation menu scrollspy to anchor section //
    $('body').scrollspy({
        target: '#navigation .navbar-collapse',
        offset: parseInt($('#navigation').height(), 0)
    });
    // End navigation menu scrollspy to anchor section //


    // sticky-menu on scroll
    $(window).on('scroll', function() {
        var scroll = $(window).scrollTop();
        if (scroll < 245) {
            $(".sticky").removeClass("sticky-menu");
        } else {
            $(".sticky").addClass("sticky-menu");
        }
    });
    // End sticky-menu on scroll


    /* magnificPopup image view */
    $('.popup-image').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        }
    });
    /* End magnificPopup image view */


    /* magnificPopup video view */
    $('.popup-video').magnificPopup({
        type: 'iframe',
        gallery: {
            enabled: true
        }
    });
    /* End magnificPopup video view */


    // jQuery tooltips //
    $('.btn-tooltip').tooltip();
    $('.btn-popover').popover();
    // End jQuery tooltips //


    // Team Slider Slick
    $('.carousel-slider.gallery-slider').slick({
        arrows: false,
        dots: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        draggable: true,
        responsive: [{
                breakpoint: 1250,
                settings: {
                    slidesToShow: 3,
                    draggable: true
                }
            },
            {
                breakpoint: 990,
                settings: {
                    slidesToShow: 1,
                    draggable: true
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 1,
                    draggable: true
                }

            }
        ]
    });
    // End Team Slider Slick


    // Projects Slider Slick
    $('.carousel-slider.projects-slider').slick({
        arrows: false,
        dots: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        draggable: true,
        responsive: [{
                breakpoint: 1200,
                settings: {
                    slidesToShow: 3,
                    draggable: true
                }
            },
            {
                breakpoint: 990,
                settings: {
                    slidesToShow: 2,
                    draggable: true
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 1,
                    draggable: true
                }

            }
        ]
    });
    // End Projects Slider Slick

    // Sponsor Slider Slick
    $('.carousel-slider.sponsor-slider').slick({
        arrows: false,
        dots: false,
        slidesToShow: 6,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 5000,
        draggable: true,
        responsive: [{
                breakpoint: 1200,
                settings: {
                    slidesToShow: 6,
                    draggable: true
                }
            },
            {
                breakpoint: 990,
                settings: {
                    slidesToShow: 4,
                    draggable: true
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 3,
                    draggable: true
                }

            }
        ]
    });
    // End Projects Slider Slick

    // Students Review Slider Slick
    $('.carousel-slider.general-slider').each(function() {
        $(this).slick({
            arrows: false,
            dots: true,
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 5000,
            draggable: true,
            responsive: [{
                breakpoint: 767,
                settings: {
                    slidesToShow: 1,
                    draggable: true
                }
            }]
        });
    });
    // End Students Review Slider Slick


    // Preview images popup gallery with Fancybox //
    $('.fancybox').fancybox({
        loop: false
    });
    // End Preview images popup gallery with Fancybox //



    // Counter animation //
    $('.themeioan_counter > h4').counterUp({
        delay: 10,
        time: 3000
    });
    // End Counter animation //


    // Navigation Burger animation //
    $('.burger-icon').on('click', function(e) {
        $(this).toggleClass('change');
        $("#navbarCollapse").slideToggle();
        e.preventDefault();
    });
    // END Navigation Burger animation //


    // Contact form submit process //
    $('#contact-us-form').submit(function() {
        var form = $(this),
            hasError = false;

        form.find('.error-msg, .success-msg').remove();

        form.find('.required-field').each(function() {
            $(this).removeClass('not-valid');
            if ($.trim($(this).val()) === '') {
                $(this).addClass('not-valid').parent().append('<div class="error-msg">This is a required field.</div>');
                hasError = true;
            } else if ($(this).hasClass('email-field')) {
                var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
                if (!emailReg.test($.trim($(this).val()))) {
                    $(this).addClass('not-valid').parent().append('<div class="error-msg">You entered an invalid Email.</div>');
                    hasError = true;
                }
            }
        });
        if (!hasError) {
            var formData = $(this).serialize();
            $.post('contact-process.php', formData, function(data) {
                form.find('.required-field').val('');
                form.append('<div class="success-msg">Thank you! We will contact you shortly.</div>');
            }).fail(function() {
                //form.find('.required-field').val('');
                form.append('<div class="error-msg">Error occurred. Please try again later.</div>');
            });
        }
        return false;
    });
    // End contact form submit process //

    // Slider Home 6 - with arrows Prev Next
    $('.owl-navigation ').owlCarousel({
        loop: true,
        margin: 0,
        nav: true,
        touchDrag: true,
        mouseDrag: true,
        autoplay: true,
        autoplayTimeout: 5000,
        smartSpeed: 1000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            }
        }
    });
    // Slider End

    // Slider Home 2
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        touchDrag: true,
        mouseDrag: true,
        autoplay: true,
        autoplayTimeout: 5000,
        smartSpeed: 1000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            }
        }
    });
    // Slider End


    //  Modifying main.js The below code is self written
    // A's Here 
    $(document).ready(function() {
        $("#discount_val").change(function(event) {
            event.preventDefault();
            var test = $('#real_val').val();
            console.log(test);
            $.ajax({
                type: 'POST',
                url: '/website/pricing-multiplier/',
                dataType: 'json',
                data: {
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").attr("value"),
                    discount: $('#discount_val').val(),
                    amount: $('#real_val').val(),
                },
                success: function(data) {
                    document.getElementById("output").innerText = data.total;
                    document.getElementById("discount").value = data.discount_applied;
                    document.getElementById("total").value = data.total;

                }

            });

        });
    });

    $(document).ready(function() {
        $("#form").submit(function(event) {
            event.preventDefault();
            $.ajax({
                type: 'POST',
                url: '/website/pricing-multiplier/',
                dataType: 'json',
                data: {
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").attr("value"),
                    discount: $('#discount_val').val(),
                    amount: $('#real_val').val(),
                },
                success: function(data) {
                    document.getElementById("output").innerText = data.total;
                    document.getElementById("discount").value = data.discount_applied;
                    document.getElementById("total").value = data.total;

                }

            });

        });
    });

});

/* Form Checks using Ajax */
// Plan Purchase Form - purchase_form.html
// $(document).ready(function() {
//     $("#zip_code").change(function(event) {
//         event.preventDefault();

//         var test = $('#zip').val();
//         console.log(test)
//         $.ajax({
//             type: 'POST',
//             url: '/website/form_validation',
//             dataType: 'json',
//             data: {
//                 csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").attr("value"),
//                 test: $('#zip_code').val(),
//                 name: $('#name').val(),

//             },
//             success: function(data) {
//                 console.log('chal gaya sayad', data.response, data.name);
//                 document.write(data.name);
//             }

//         });

//     });
// });

// form.find('.required-field').each(function() {
//     $(this).removeClass('not-valid');
//     if ($.trim($(this).val()) === '') {
//         $(this).addClass('not-valid').parent().append('<div class="error-msg">This is a required field.</div>');
//         hasError = true;
//     } else if ($(this).hasClass('email-field')) {
//         var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
//         if (!emailReg.test($.trim($(this).val()))) {
//             $(this).addClass('not-valid').parent().append('<div class="error-msg">You entered an invalid Email.</div>');
//             hasError = true;
//         }
//     }
// });


$("#zip_code").change(function(event) {
    // if ($('#zip_code').val() >= 6) 
    if ($('.error-msg').length >= 1) {
        $('.error-msg').empty()
        console.log("if chala")
    }
    // if (document.getElementById('error_div').innerText.length >= 1) {
    //     $('.error-msg').empty()
    //     console.log("if chala")
    // }
    var x = document.getElementById('zip_code').value
    var div = document.createElement('div');
    div.classList.add('error-msg');
    div.setAttribute('id', 'error_div')

    var numbers = /^[0-9]+$/;
    if (!x.match(numbers)) {
        console.log("if chala")
        div.innerText = "alphabets are not valid";
        document.getElementById('div_zip').appendChild(div);
    } else {
        if (x.length > 6) {
            div.innerText = "Zip code should not be greater then 6 digits";
            document.getElementById('div_zip').appendChild(div);
        }

        if (x.length < 3) {
            div.innerText = "Zip code should not be less then 3 digits";
            document.getElementById('div_zip').appendChild(div);

        }
        // $(this).parent().append('<div class="error-msg">This is a required field.</div>');
    }
});

$("#phone").change(function(event) {
    var test = document.getElementsByClassName('error-msg');
    for (i = 0; i <= test.length; i++) {
        if (test[i]) // Exception avoiding if
            test[i].remove()
    }
    var x = document.getElementById('phone').value
    var div = document.createElement('div');
    div.classList.add('error-msg');
    div.setAttribute('id', 'error_div')

    var numbers = /^[0-9]+$/;
    if (!x.match(numbers)) {
        console.log("if chala")
        div.innerText = "alphabets are not valid";
        document.getElementById('div_phone').appendChild(div);
    } else {
        if (x.length < 10) {
            div.innerText = "Phone code should not be less then 10 digits";
            document.getElementById('div_phone').appendChild(div);

        }
        if (x.length > 10) {
            div.innerText = "Phone code should not be greater then 10 digits";
            document.getElementById('div_phone').appendChild(div);
        }
    }
});





//Typed Text Start
document.addEventListener('DOMContentLoaded', function() {

    'use strict';

    if ($("#typed")[0]) {
        var typed = new Typed('#typed', {
            stringsElement: '#typed-strings',
            typeSpeed: 90,
            backSpeed: 90,
            startDelay: 1500,
            loop: true,
            loopCount: Infinity,
            onComplete: function(self) {
                prettyLog('onComplete ' + self);
            },
            preStringTyped: function(pos, self) {
                prettyLog('preStringTyped ' + pos + ' ' + self);
            },
            onStringTyped: function(pos, self) {
                prettyLog('onStringTyped ' + pos + ' ' + self);
            },
            onLastStringBackspaced: function(self) {
                prettyLog('onLastStringBackspaced ' + self);
            },
            onTypingPaused: function(pos, self) {
                prettyLog('onTypingPaused ' + pos + ' ' + self);
            },
            onTypingResumed: function(pos, self) {
                prettyLog('onTypingResumed ' + pos + ' ' + self);
            },
            onReset: function(self) {
                prettyLog('onReset ' + self);
            },
            onStop: function(pos, self) {
                prettyLog('onStop ' + pos + ' ' + self);
            },
            onStart: function(pos, self) {
                prettyLog('onStart ' + pos + ' ' + self);
            },
            onDestroy: function(self) {
                prettyLog('onDestroy ' + self);
            }
        });
    } else {
        // Do something if class does not exist
    }


});

function prettyLog(str) {}
//Typed Text End