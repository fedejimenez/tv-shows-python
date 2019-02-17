function get_more_info(id){
  get_next_episode(id);
  get_cast(id);
}

function get_next_episode(id) {
  $.ajax({
      url:  'http://api.tvmaze.com/shows/'+id+'?embed=nextepisode',
      type:  'get',
      dataType:  'json',
      success: function  (data) {
        if (data.hasOwnProperty('_embedded')) {
          let nextepisode = data['_embedded']['nextepisode']['airdate'];
          document.querySelector('#next-episode').innerHTML = "<i class='fas fa-calendar pr-1'></i> Next Ep.: " + nextepisode;
        }
      },
      error: function(e){
        console.log(e);
      }
  });
}

function get_cast(id) {
  $.ajax({
      url:  'http://api.tvmaze.com/shows/'+id+'/cast',
      type:  'get',
      dataType:  'json',
      success: function  (data) {
        console.log(data);
        let cast = [];
        let length = data.length; 
        if (data.length > 9){
          length = 10 
        }

        if (length == 0){
          cast = "Oops! There is no information about the cast.";
        }else{
          for (let i = 0; i < length; i++) {
            let obj = data[i];
              cast.push(" " + obj['person']['name']);
          }
        }

        document.querySelector('#cast').innerHTML = cast ;
      },
      error: function(e){
        console.log(e);
      }
  });
}

// Autocomplete search
$(document).ready(function(){
    $("#input-search").keyup(function(){
        let search = $(this).val();
        if (search.length == 0) {
          $("#spinner-search").addClass('d-none');
          $("#section-search").removeClass('d-none');
        }
        if (search.length > 0 && search.length < 3){
          $("#spinner-search").removeClass('d-none');
          $("#section-search").addClass('d-none');
          $("#search-result").empty();
        }else if (search.length > 3){
          $("#spinner-search").addClass('d-none');
          $("#section-search").addClass('d-none');

          $.ajax({
              url: 'http://api.tvmaze.com/search/shows?q='+search,
              type: 'get',
              dataType: 'json',
              success:function(response){
                if (response){
                  let len = response.length;
                  if (response.length == 0) {
                    $("#spinner-search").removeClass('d-none');
                    $("#search-result").empty();
                  }
                  $("#search-result").empty();
                  for( let i = 0; i<len; i++){
                    let name = response[i]['show']['name'];
                    let rating = response[i]['show']['rating']['average'];
                    let img ='https://via.placeholder.com/150' ; 
                    if (response[i]['show']['image'] != null) {
                      img = response[i]['show']['image']['medium'];
                    }

                    if (rating == null){
                      rating = "";
                    } 
                    $("#search-result").append("<a href='http://localhost:8000/?name="
                                                +name.toLowerCase()
                                                +"'> <li class='list-group-item d-flex justify-content-between align-items-center'>"
                                                +"<img src="+img+">"+name
                                                +"<span class='badge badge-primary badge-pill'>"+ rating +"</span>"
                                                +"</li></a>");

                  }
                }
              },
              error: function(e){
                console.log(e);
              }
          });
        }
    });
});
