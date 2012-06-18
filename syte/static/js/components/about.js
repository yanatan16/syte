
function setupAbout(el) {
  var href = el.href;

  var spinner = new Spinner(spin_opts).spin();
  $('#about-link').append(spinner.el);

  require(["json!/about/", "text!templates/about-me-view.html"],
     function(about_data, about_view) {
         if (about_data.error || about_data.length == 0) {
             window.location = href;
             return;
         }

         var template = Handlebars.compile(about_view);

         $(template(about_data)).modal().on('hidden', function () {
             $(this).remove();
             adjustSelection('home-link');
         })

         spinner.stop();
      });
}
