"use strict";
var player; // Declare the player variable globally

        document.addEventListener("DOMContentLoaded", function() {
            const portfolioItems = document.querySelectorAll('.portfolio-item');
            portfolioItems.forEach(function(item) {
                item.addEventListener('click', function() {
                    const videoId = this.getAttribute('data-video-url');
                    console.log("videoID : " + videoId);

                    const modalBody = document.querySelector('.modal-body');
                    modalBody.innerHTML = `<p>타이틀: ${this.querySelector('.card-title').textContent}</p>
                                           <p>내용: ${this.querySelector('.card-text').textContent}</p>
                                           <div id="player"></div>`; // Placeholder for the player

                    // Instantiate modal with Bootstrap
                    const modal = new bootstrap.Modal(document.getElementById('portfolioModal'), {
                        keyboard: true
                    });
                    modal.show();

                    // This function initializes the YouTube player in the modal
                    function onYouTubeIframeAPIReady() {
                        player = new YT.Player('player', {
                            height: '360',
                            width: '640',
                            videoId: videoId,
                            events: {
                                'onReady': onPlayerReady,
                                'onStateChange': onPlayerStateChange
                            }
                        });
                    }
                    onYouTubeIframeAPIReady(); // Call to create the YouTube player
                });
            });

            // 닫기
            const modal = document.getElementById('portfolioModal');
            modal.addEventListener('hidden.bs.modal', function () {
                if (player) {
                    player.stopVideo(); // Stop video playback when modal is closed
                }
            });
        });

        function onPlayerReady(event) {
            event.target.playVideo(); // Autoplay the video when player is ready
        }

        function onPlayerStateChange(event) {
            // Example: do something when the video state changes
        }

// 더보기 클릭했을때
document.getElementById("loadMoreVlog").addEventListener("click", function() {
  // console.log("버튼 클릭함 ")
    var items = document.querySelectorAll('#sub-vlog .portfolio-item');
    items.forEach(function(item, index) {
        if (index >= 4) { // 처음 4개는 제외하고 보여주기
            item.style.display = 'block';
        }
    });
    this.style.display = 'none'; // "더 보기" 버튼 숨기기
});
document.getElementById("loadMoreEnterprise").addEventListener("click", function() {
    var items = document.querySelectorAll('#sub-enterprise .portfolio-item');
    items.forEach(function(item, index) {
        if (index >= 4) {
            item.style.display = 'block';
        }
    });
    this.style.display = 'none';
});

document.getElementById("loadMoreProduct").addEventListener("click", function() {
    var items = document.querySelectorAll('#sub-product .portfolio-item');
    items.forEach(function(item, index) {
        if (index >= 4) {
            item.style.display = 'block';
        }
    });
    this.style.display = 'none';
});