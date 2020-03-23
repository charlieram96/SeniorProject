var videoList = ["https://storage.googleapis.com/coverr-main/mp4/Mt_Baker.mp4", "https://storage.googleapis.com/coverr-main/mp4/Underground-Traffic.mp4", "/static/videos/stars.mp4", "/static/videos/seoul_traffic.mp4", "/static/videos/night_traffic.mp4", "/static/videos/pedestrians.mp4", "/static/videos/traffic1.mp4"];
videoList.sort(function(a, b) {
  return 0.5 - Math.random()
});

$("#videos").html("<video id='bgvid' autoplay loop muted playsinline><source src='" + videoList[0] + "' type='video/mp4'></video>");

