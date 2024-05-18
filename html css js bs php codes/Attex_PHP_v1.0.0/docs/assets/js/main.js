(function ($) {
  'use strict';

  // Activate Tooltips & Popovers
  $(function () {
    $('[data-toggle="tooltip"]').tooltip();
    $('[data-toggle="popover"]').popover();

    // Dismiss Popovers on next click
    $('.popover-dismiss').popover({
      trigger: 'focus'
    })
  });

  $(document).on('ready', function () {
    // Go to Top
    var go2TopShowHide = (function () {
      var $this = $('.js-go-to');

      $this.on("click", function(event) {
        event.preventDefault();
        $("html, body").animate({scrollTop: 0}, 600);
      });

      var go2TopOperation = function() {
        var CurrentWindowPosition = $(window).scrollTop();

        if (CurrentWindowPosition > 400) {
          $this.addClass("show");
        } else {
          $this.removeClass("show");
        }
      };

      go2TopOperation();

      $(window).scroll(function() {
        go2TopOperation();
      });
    }());
  });

  $(window).on('load', function () {

    // Page Nav
    var onePageScrolling = (function () {
      $('.js-scroll-nav a').on('click', function(event) {
        event.preventDefault();
        if ( $('.duik-header').length ) {
          $('html, body').animate( {scrollTop:( $('#' + this.href.split('#')[1]).offset().top - ( $('.duik-header .navbar').height() ) - 30 )}, 600 );
        } else {
          $('html, body').animate( {scrollTop:( $('#' + this.href.split('#')[1]).offset().top - 30 )}, 600 );
        }
      });
    }());

    var oneAnchorScrolling = (function () {
      $('.js-anchor-link').on('click', function(event) {
        event.preventDefault();
        if ( $('.duik-header').length ) {
          $('html, body').animate( {scrollTop:( $('#' + this.href.split('#')[1]).offset().top - ( $('.duik-header .navbar').height() ) - 30 )}, 600 );
        } else {
          $('html, body').animate( {scrollTop:( $('#' + this.href.split('#')[1]).offset().top - 30 )}, 600 );
        }
      });
    }());
  });

})(jQuery);


class MenuElement extends HTMLElement{
  connectedCallback(){
    this.innerHTML = `<nav class="col-md-3 col-xl-2 bg-light duik-sidebar navbar-expand-md">

        <!-- Sidebar Nav -->
        <div class="collapse navbar-collapse" id="sidebar-nav">
          <div class="js-scrollbar duik-sidebar-sticky">
            <h5 class="duik-sidebar__heading">Documentation</h5>
            <ul class="duik-sidebar__nav">
              <li class="duik-sidebar__item">
                <a class="duik-sidebar__link" href="./index.html"> Introduction </a>
              </li>
              <li class="duik-sidebar__item"><a class="duik-sidebar__link" href="./pages-installation.html">Getting
                  Started</a></li>
                  <li class="duik-sidebar__item">
                <a class="duik-sidebar__link" href="./pages-changelog.html">Change log</a>
              </li>
<!--              <li class="duik-sidebar__item"><a class="duik-sidebar__link" href="./pages-strcuture.html">File-->
<!--                  Strcuture</a></li>-->
<!--              <li class="duik-sidebar__item"><a class="duik-sidebar__link" href="./pages-routing.html">Routing</a></li>-->
<!--              <li class="duik-sidebar__item"><a class="duik-sidebar__link" href="./pages-spliting.html">Code-->
<!--                  Spliting</a></li>-->
            </ul>
<!--            <h5 class="duik-sidebar__heading">Customization</h5>-->
<!--            <ul class="duik-sidebar__nav">-->
<!--              <li class="duik-sidebar__item"><a class="duik-sidebar__link" href="./pages-customization.html">Layouts</a>-->
<!--              </li>-->
<!--            </ul>-->

<!--            <h5 class="duik-sidebar__heading">Other</h5>-->
<!--            <ul class="duik-sidebar__nav">-->
<!--              <li class="duik-sidebar__item">-->
<!--                <a class="duik-sidebar__link" href="./pages-changelog.html">Change log</a>-->
<!--              </li>-->
<!--            </ul>-->
          </div>
        </div>
        <!-- End Sidebar Nav -->
      </nav>`;
  }
}
customElements.define('x-menu', MenuElement);
