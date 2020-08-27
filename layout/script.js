$(document).on('click','#little',function ()  {
    $( this ).slideUp();
  });

$(document).on('click','#littleNews',function () {
    swal({
        title: "Good job!",
        text: "You clicked the button!",
        icon: "success",
      });
        });