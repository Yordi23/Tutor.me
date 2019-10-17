  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  } 

  async function ReloadPage(){
    await sleep(50)
    window.location.reload(true);

  };

  function CreateRequest(element){
    $.ajax({
      method: "POST",
      url: '/CreateRequest/',
      dataType: "json",
      async: true,
      data: {
        Tutor_User: element,  
    },
    });
    ReloadPage();
  };

  function CancelRequest(element){
    
    $.ajax({
      method: "POST",
      url: '/CancelRequest/',
      dataType: "json",
      async: true,
      data: {
        csrfmiddlewaretoken:"{{ csrf_token }}",
        request_id: element,  
    },
    });
    ReloadPage();
  };

  function AcceptRequest(element){
    
    $.ajax({
      method: "POST",
      url: '/AcceptRequest/',
      dataType: "json",
      async: true,
      data: {
        csrfmiddlewaretoken:"{{ csrf_token }}",
        request_id: element,  
    },
    });
    ReloadPage();
  };

  function RejectRequest(element){
    
    $.ajax({
      method: "POST",
      url: '/RejectRequest/',
      dataType: "json",
      async: true,
      data: {
        csrfmiddlewaretoken:"{{ csrf_token }}",
        request_id: element,  
    },
    });
    ReloadPage();

  };


