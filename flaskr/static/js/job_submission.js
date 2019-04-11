$(document).ready(function() {
   //On pressing a key on "Search box" in "index.html" file. This function will be called.
   $("#search").keyup(function(e) {
     //checks if keyup is enter
     if(e.which == 13) {
       if ($("#search").val()==""){
         alert("Please enter the url")
         return
       }
       $.ajax({
           type: "POST",
           url: "/job_submission",
           data: {
               entered_text:$("#search").val()
           },
           success: function(response) {
             $('#display_search').html(response.tasks_count)
           },error: function (request, status, error) {

                  alert(request.responseText);
              }
       });
     }
 });

 $('#go_btn').on('click',function(){
   $.ajax({
       type: "POST",
       url: "/job_submission",
       data: {
           entered_text:$("#search").val()
       },
       success: function(response) {
         $('#display_search').html(response.tasks_count)
       },error: function (request, status, error) {
              alert(request.responseText);
          }
   });
 });
});
