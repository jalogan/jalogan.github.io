document.addEventListener('DOMContentLoaded', () => {
  console.log("Custom swipe initialized");

  let isSwiping = false;
  let swipeDirection = null;        // 'left' or 'right'
  let isTransitioning = false;

  const body = document.body;       // now guaranteed
  const homePage = body.classList.contains('home-page');
  const sidebar = document.querySelector('#sidebar');

  // Lock page rendering during swipe (disable scroll)
  function lockPageRendering() {
    body.style.overflow = 'hidden';
    console.log('Page locked during swipe');
  }

  // Unlock page rendering after swipe
  function unlockPageRendering() {
    body.style.overflow = '';
    console.log('Page unlocked after swipe');
  }

  // Function to load the /about-me page dynamically into the sidebar
  function loadSidebarContent() {
    if (!sidebar) return;

    sidebar.innerHTML = '<div class="loading">Loading...</div>';

    fetch('/about-me')
      .then(response => response.text())
      .then(html => {
        sidebar.innerHTML = html;
        console.log("Loaded /about-me into the sidebar.");
      })
      .catch(error => {
        console.error('Error loading /about-me content:', error);
        sidebar.innerHTML = '<div class="error">Failed to load content.</div>';
      });
  }

  function restoreHomepage() {
    if (sidebar) sidebar.innerHTML = '';
  }

  function handleSwipe() {
    if (!homePage) return;
    if (isTransitioning) return;

    if (swipeDirection === 'left') {
      body.classList.add('sidebar-active');
      loadSidebarContent();
      console.log("Moved homepage to sidebar and loaded /about-me content");

      isTransitioning = true;
      setTimeout(() => {
        unlockPageRendering();
        isTransitioning = false;
      }, 500);
    } else if (swipeDirection === 'right') {
      body.classList.remove('sidebar-active');
      restoreHomepage();
      console.log("Restored homepage");
      unlockPageRendering();
      isTransitioning = false;
    }
  }

  function detectSwipe(event) {
    const touchstartX = event.touches ? event.touches[0].clientX : event.clientX;
    const touchstartY = event.touches ? event.touches[0].clientY : event.clientY;
    let touchendX, touchendY;

    function handleTouchMove(e) {
      touchendX = e.touches ? e.touches[0].clientX : e.clientX;
      touchendY = e.touches ? e.touches[0].clientY : e.clientY;

      const horizontalSwipe =
        Math.abs(touchstartX - touchendX) > Math.abs(touchstartY - touchendY);

      if (!horizontalSwipe) return;

      if (touchstartX > touchendX && !isSwiping) {
        swipeDirection = 'left';
        isSwiping = true;
        lockPageRendering();
        console.log("Left swipe detected");
        handleSwipe();
      } else if (touchstartX < touchendX && !isSwiping) {
        swipeDirection = 'right';
        isSwiping = true;
        lockPageRendering();
        console.log("Right swipe detected");
        handleSwipe();
      }
    }

    function handleTouchEnd() {
      if (isSwiping) {
        isSwiping = false;
        console.log("Swipe transition complete");
      }
      document.removeEventListener('touchmove', handleTouchMove);
      document.removeEventListener('touchend', handleTouchEnd);
    }

    document.addEventListener('touchmove', handleTouchMove, { passive: false });
    document.addEventListener('touchend', handleTouchEnd);
  }

  function detectMouseSwipe(event) {
    const touchstartX = event.clientX;
    const touchstartY = event.clientY;
    let touchendX, touchendY;

    function handleMouseMove(e) {
      touchendX = e.clientX;
      touchendY = e.clientY;

      const horizontalSwipe =
        Math.abs(touchstartX - touchendX) > Math.abs(touchstartY - touchendY);

      if (!horizontalSwipe) return;

      if (touchstartX > touchendX && !isSwiping) {
        swipeDirection = 'left';
        isSwiping = true;
        lockPageRendering();
        console.log("Mouse left swipe detected");
        handleSwipe();
      } else if (touchstartX < touchendX && !isSwiping) {
        swipeDirection = 'right';
        isSwiping = true;
        lockPageRendering();
        console.log("Mouse right swipe detected");
        handleSwipe();
      }
    }

    function handleMouseUp() {
      if (isSwiping) {
        isSwiping = false;
        console.log("Mouse swipe transition complete");
      }
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
    }

    document.addEventListener('mousemove', handleMouseMove, { passive: false });
    document.addEventListener('mouseup', handleMouseUp);
  }

  // Only activate swipe functionality on homepage
  if (homePage) {
    document.addEventListener('touchstart', detectSwipe, { passive: true });
    document.addEventListener('mousedown', detectMouseSwipe);
  }
});
