// Custom Scripts for Primal Template //
if ( window.history.replaceState ) {
  window.history.replaceState( null, null, window.location.href );
}


jQuery(function($) {
    "use strict";


        // get the value of the bottom of the #main element by adding the offset of that element plus its height, set it as a variable
        var mainbottom = $('#main').offset().top;

        // on scroll,
        $(window).on('scroll',function(){

        // we round here to reduce a little workload
        stop = Math.round($(window).scrollTop());
        if (stop > mainbottom) {
            $('.navbar').addClass('past-main');
            $('.navbar').addClass('effect-main')
        } else {
            $('.navbar').removeClass('past-main');
       }

      });


  // Collapse navbar on click

   $(document).on('click.nav','.navbar-collapse.in',function(e) {
    if( $(e.target).is('a') ) {
    $(this).removeClass('in').addClass('collapse');
   }
  });

  /*-----------------------------------
  ----------- Scroll To Top -----------
  ------------------------------------*/

    $(window).scroll(function () {
      if ($(this).scrollTop() > 1000) {
          $('#back-top').fadeIn();
      } else {
          $('#back-top').fadeOut();
      }
    });
    
    
    // scroll body to 0px on click
    $('#back-top').on('click', function () {
      $('#back-top').tooltip('hide');
      $('body,html').animate({
          scrollTop: 0
      }, 1500);
      return false;
    });


  /*-------- Owl Carousel ---------- */
    $(".reviews").owlCarousel({

    slideSpeed : 200,
    items: 1,
    singleItem: true,
    autoPlay : true,
    pagination : false
    });


  /*-------- Owl Carousel ---------- */
    $(".review-cards").owlCarousel({

    slideSpeed : 200,
    items: 1,
    singleItem: true,
    autoPlay : true,
    pagination : false
    });


  /* ------ jQuery for Easing min -- */

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').on('click', function () {
      if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
          $('html, body').animate({
            scrollTop: (target.offset().top - 54)
          }, 1000, "easeInOutExpo");
          return false;
        }
      }
    });


  /* --------- Wow Init ------ */

  new WOW().init();


  /* ------ Countdown ----- */


/*----- Preloader ----- */


/*----- Subscription Form ----- */



// Accordion //

function toggleChevron(e) {
   $(e.target)
     .prev('.panel-heading')
     .find("span.glyphicon")
     .toggleClass('glyphicon-chevron-down glyphicon-chevron-right');
 }
 $('#accordion').on('hide.bs.collapse show.bs.collapse', toggleChevron);



});




function rate(){
 // document.body.style.opacity = 0.5;
  cc = ``;
 
 
let rt = document.querySelector('.rt');
rt.style.display = 'block';
// rt.innerHTML = cc;
 
 let rate = document.querySelector('.rate');
 // rate.style.opacity = 1;
 
 var elem = document.querySelector('input[type="range"]');

 let s = document.querySelector('.s');
 let s1 = document.querySelector('.s1');
 let s2 = document.querySelector('.s2');
 let s3 = document.querySelector('.s3');
 let s4 = document.querySelector('.s4');
 
var rangeValue = function() {
  var newValue = elem.value;
  var target = document.querySelector('.value');
  target.innerHTML = newValue;
  
 if(newValue <= 1){
   s.style.color = '#A2A5BE';
   s1.style.color = '#A2A5BE';
   s2.style.color = '#A2A5BE';
   s3.style.color = '#A2A5BE';
   s4.style.color = '#A2A5BE';
 }else if(newValue <= 2){
   s.style.color = 'yellow';
   s1.style.color = '#A2A5BE';
   s2.style.color = '#A2A5BE';
   s3.style.color = '#A2A5BE';
   s4.style.color = '#A2A5BE';
 }else if(newValue <= 2.8){
   s.style.color = 'yellow';
   s1.style.color = 'yellow';
   s2.style.color = '#A2A5BE';
   s3.style.color = '#A2A5BE';
   s4.style.color = '#A2A5BE';
 }else if(newValue <= 3.8){
   s.style.color = 'yellow';
   s1.style.color = 'yellow';
   s2.style.color = 'yellow';
   s3.style.color = '#A2A5BE';
   s4.style.color = '#A2A5BE';
 }else if(newValue <= 4.8){
   s.style.color = 'yellow';
   s1.style.color = 'yellow';
   s2.style.color = 'yellow';
   s3.style.color = 'yellow';
   s4.style.color = '#A2A5BE';
 }else if(newValue <= 6){
   s.style.color = 'yellow';
   s1.style.color = 'yellow';
   s2.style.color = 'yellow';
   s3.style.color = 'yellow';
   s4.style.color = 'yellow';
   
 }
}

elem.addEventListener("input", rangeValue);



}





function nn(crn) {
  if (crn == 'anonim') {
    let kr = document.querySelector('.kr');
    kr.innerHTML = `
<input class="form-control rn krn" type="text" placeholder="Anonymus" name='nama' aria-label="default input example" disabled >`;
    let kdl = document.querySelector('.kdl');
    let kbar = document.querySelector('.kbar');
    kdl.style.background = 'white';
    kbar.style.background = 'gray';

  } else {
    let kbar = document.querySelector('.kbar');
    let kdl = document.querySelector('.kdl');
    kdl.style.background = 'gray';
    kbar.style.background = 'white';

    let kr = document.querySelector('.kr')
    kr.innerHTML = `
<input class="form-control rn krn" type="text" placeholder="Name.." name='nama' aria-label="default input example">`;

  }
}

function na(){
    let rate = document.querySelector('.rate');
    rate.style.display = 'none';
    //document.body.style.opacity = 1;
}

function nu(){
    alert('Okee Terima kasih..!! Okay, Thanks..!!')
    let rate = document.querySelector('.rate');
    rate.style.display = 'none';
    //document.body.style.opacity = 1;
    document.getElementById("myForm").reset();
}



function loading(){
    let tpre = document.querySelector('.tpre');
    
   tpre.style.display = 'block';
}


// let rateData = {'NAME': [], 'RATE':[], 'MESSAGE':[]};
// const rateDb = 'rateDb';



// function rateWrite(acct, what, item){
//   switch(acct){
//     case 'ADD':
//       rateData[what].push(item);
//       break;
//     case 'REMOVE':
//       rateData[what].push(item);
//       break;
//     case 'UPDATE':
//       break;
//     case 'ADD':
//       break;
    
//   }
  
//   console.log(rateData)
  
//   localStorage.setItem(rateDb, JSON.stringify(rateData))
//   return
// }

// function rateConnect() {
//   let val = document.querySelector('.valrate').value;
//   let rn = document.querySelector('.rn').value;
//   let ulas = document.querySelector('.ulas').value;

//   console.log(val);

//   rateWrite('ADD', 'NAME', rn)
//   rateWrite('ADD', 'RATE', val)
//   rateWrite('ADD', 'MESSAGE', ulas)
// }


// function coba(){
//   var movies = {
//     'title': 'Spiderman',
//     'release_date': '20-01-2022'
//   }
  
//   $.ajax({
//       url: Flask.url_for('/function_route'),
//       type: 'POST',
//       data: JSON.stringify(movies),
//     })
//     .done(function(result) { 
//       alert(result)
//     })
// }


function step1(){
 let busing = document.querySelector('.but');
 let penutup = document.querySelector('.using-penutup');
 penutup.style.display="block";

 busing.addEventListener('click',()=>{
  penutup.style.display="none";
})
}

function tampUl(){
  let ul = document.querySelector('.con-ulasan');
  ul.style.display = 'block';
}

function semUl(){
  let ul = document.querySelector('.con-ulasan');
  ul.style.display = 'none';
}


