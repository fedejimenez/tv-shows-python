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
        let cast = [];
        for (let i = 0; i < 10; i++) {
          let obj = data[i];
          cast.push(" " + obj['person']['name']);
        }
        document.querySelector('#cast').innerHTML = cast ;
      },
      error: function(e){
        console.log(e);
      }
  });
}
