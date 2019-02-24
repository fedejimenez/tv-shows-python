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
                    let img ='http://placehold.jp/24/cccccc/ffffff/150x150.png?text=No%20image%20avaiable' ; 
                    let genres = response[i]['show']['genres'];
                    let array_genres = [];
                    for (var j = genres.length - 1; j >= 0; j--) {
                      array_genres.push(" <span class='badge badge-primary ml-2'>"
                             +       genres[j]
                             +  "</span>")
                    }

                    let status = response[i]['show']['status'];
                    if (response[i]['show']['image'] != null) {
                      img = response[i]['show']['image']['medium'];
                    }

                    if (rating == null){
                      rating = "";
                    } 
                    $("#search-result").append(""
                                                + " <div class='col-sm-4 mb-2'>"
                                                + "   <div class='card card-cascade'>"
                                                + "      <div class='view overlay'>"
                                                + "        <a href='https://tvshowspython.herokuapp.com/?name="+name+"'>"
                                                + "          <img class='card-img-top img-fluid' src='"+ img +"' alt='Card image cap' >"
                                                + "            <div class='mask flex-center rgba-blue-strong'>"
                                                + "              <h1 class='white-text text-justify'><strong>"+rating+" / 10 </strong></h1>"
                                                + "            </div>"
                                                + "        </a>"
                                                + "      </div>"
                                                + "      <a href='https://tvshowspython.herokuapp.com/?name="+name+"'>"
                                                + "         <div class='card-body card-body-cascade'>"
                                                + "           <h3 class='card-title text-center black-text'>"
                                                + "             <strong>"+ name 
                                                + "             </strong>"
                                                + "           </h3>"
                                                + "           <p class='card-text text-center'>"
                                                + "             <span class='mr-3'><i class='fas fa-hourglass pr-1'></i>"
                                                + "               <strong>"
                                                +                   status 
                                                + "               </strong>"
                                                + "             <span>"
                                                +               array_genres.join(' ')
                                                + "           </p>"
                                                + "         </div>"
                                                + "      </a>"
                                                + "   </div>"
                                                + " </div>"
                                              );

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


function change_random(){
  let random = Math.floor((Math.random() * 41014) + 1);
  let input_field = document.getElementById("input-random");
  input_field.setAttribute("value", random.toString());
}
