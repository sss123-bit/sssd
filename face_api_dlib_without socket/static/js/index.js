const video = document.getElementById('video');

navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
Promise.all([
  faceapi.loadFaceLandmarkModel("/static/models/"),
  faceapi.loadFaceRecognitionModel("/static/models/"),
  faceapi.loadTinyFaceDetectorModel("/static/models/"),
  faceapi.loadFaceLandmarkModel("/static/models/"),
  faceapi.loadFaceLandmarkTinyModel("/static/models/"),
  faceapi.loadFaceRecognitionModel("/static/models/"),
  faceapi.loadFaceExpressionModel("/static/models/"),
])
  .then(startVideo)
  .catch(err => console.error(err));

function startVideo() {
  console.log("access");
  navigator.getUserMedia(
    {
      video: {}
    },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}

video.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video);
  document.body.append(canvas);
  const displaySize = { width: video.width, height: video.height };
  faceapi.matchDimensions(canvas, displaySize);


  setInterval(async () => {
    const detections = await faceapi
      .detectAllFaces(video, new faceapi.TinyFaceDetectorOptions())
      .withFaceLandmarks()
      .withFaceExpressions();
    


    const resizedDetections = faceapi.resizeResults(detections, displaySize);
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
    faceapi.draw.drawDetections(canvas, resizedDetections);

    console.log(detections);
  }, 100)
})
