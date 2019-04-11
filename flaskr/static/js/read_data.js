$(document).ready(function() {
  function funcName() {
           $.ajax({
               type: "POST",
               url: "/read_data",
               success: function(response) {
                $('#display_search').html(response.tasks_running)
                $('#job_rows').html(response.row_tags)
               },error: function (request, status, error) {
                    console.log(request.responseText);
                  }
           });
  }
  setInterval(funcName, 2000);
});
