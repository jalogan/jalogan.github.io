console.log("Custom swipe initialized");

let isSwiping = false;
let swipeDirection = null; // Direction of the swipe (left or right)
let isTransitioning = false; // Prevents multiple transitions at the same time
let homePage = document.body.classList.contains('home-page'); // Check if we're on the homepage
let sidebar = document.querySelector('#sidebar'); // Make sure you have a sidebar container

// Lock page rendering during swipe (disable scroll)
function lockPageRendering() {
  document.body.style.overflow = 'hidden'; // Prevent scrolling during swipe
  console.log('Page locked during swipe');
}

// Unlock page rendering after swipe
function unlockPageRendering() {
  document.body.style.overflow = ''; // Re-enable scrolling after swipe
  console.log('Page unlocked after swipe');
}

// Function to load the /about-me page dynamically into the sidebar
function loadSidebarContent() {
  if (!sidebar) return;

  // Clear current content in the sidebar (if any)
  sidebar.innerHTML = '<div class="loading">Loading...</div>';  // Optional: Show a loading message

  // Fetch the /about-me page content dynamically
  fetch('/about-me')
    .then(response => response.text())
    .then(html => {
      // Inject the /about-me content into the sidebar
      sidebar.innerHTML = html;
      console.log("Loaded /about-me into the sidebar.");
    })
    .catch(error => {
      console.error('Error loading /about-me content:', error);
      sidebar.innerHTML = '<div class="error">Failed to load content.</div>'; // Show error if loading fails
    });
}

// Function to handle the swipe transition
function handleSwipe() {
  if (!homePage) return; // Only enable swipe on the homepage
  
  const body = document.body;

  // When swiping left, move the homepage content to the side and load the sidebar content
  if (swipeDirection === 'left') {
    body.classList.add('sidebar-active');  // This will move homepage content to the side
    loadSidebarContent();  // Load the /about-me content into the sidebar
    console.log("Moved homepage to sidebar and loaded /about-me content");

    isTransitioning = true;
    // Allow transition to finish and unlock page
    setTimeout(() => {
      unlockPageRendering();
      isTransitioning = false;
    }, 500); // Adjust transition time if needed
  } else if (swipeDirection === 'right') {
    // When swiping right, move the homepage back to its original position
    body.classList.remove('sidebar-active');
    restoreHomepage(); // Restore the homepage content
    console.log("Restored homepage");
  }
}

// Function to restore the homepage content when swiping right
function restoreHomepage() {
  const sidebar = document.querySelector('#sidebar'); // Get sidebar
  
  // Clear sidebar content when restoring homepage
  if (sidebar) {
    sidebar.innerHTML = ''; // Clear sidebar content
  }

  // Optionally reset any additional elements if needed
}

// Detect swipe events
function detectSwipe(event) {
  const touchstartX = event.touches ? event.touches[0].clientX : event.clientX;
  const touchstartY = event.touches ? event.touches[0].clientY : event.clientY;
  let touchendX, touchendY;

  function handleTouchMove(e) {
    touchendX = e.touches ? e.touches[0].clientX : e.clientX;
    touchendY = e.touches ? e.touches[0].clientY : e.clientY;

    // Only allow left and right swipes (horizontal)
    const horizontalSwipe = Math.abs(touchstartX - touchendX) > Math.abs(touchstartY - touchendY);

    if (horizontalSwipe) {
      // If swipe is to the left, trigger left swipe action
      if (touchstartX > touchendX && !isSwiping) {
        swipeDirection = 'left';
        isSwiping = true;
        lockPageRendering(); // Lock page during swipe
        console.log("Left swipe detected");

        handleSwipe(); // Perform the left swipe action
      }
      // If swipe is to the right, trigger right swipe action (restores homepage)
      else if (touchstartX < touchendX && !isSwiping) {
        swipeDirection = 'right';
        isSwiping = true;
        lockPageRendering(); // Lock page during swipe
        console.log("Right swipe detected");

        handleSwipe(); // Perform the right swipe action
      }
    }
  }

  function handleTouchEnd() {
    // Reset the swipe flag after the move ends
    if (isSwiping) {
      isSwiping = false;
      console.log("Swipe transition complete");
    }
  }

  document.addEventListener('touchmove', handleTouchMove, { passive: false });
  document.addEventListener('touchend', handleTouchEnd);
}

// Only activate swipe functionality on homepage
document.addEventListener('DOMContentLoaded', () => {
  if (homePage) {
    // Only activate swipe functionality on homepage
    document.addEventListener('touchstart', detectSwipe);
  }
});

// Optional: For Desktop (Mouse Swipes)
function detectMouseSwipe(event) {
  const touchstartX = event.clientX;
  const touchstartY = event.clientY;
  let touchendX, touchendY;

  function handleMouseMove(e) {
    touchendX = e.clientX;
    touchendY = e.clientY;

    // Only allow left and right swipes (horizontal)
    const horizontalSwipe = Math.abs(touchstartX - touchendX) > Math.abs(touchstartY - touchendY);

    if (horizontalSwipe) {
      // If swipe is to the left, trigger left swipe action
      if (touchstartX > touchendX && !isSwiping) {
        swipeDirection = 'left';
        isSwiping = true;
        lockPageRendering(); // Lock page during swipe
        console.log("Mouse left swipe detected");

        handleSwipe(); // Perform the left swipe action
      }
      // If swipe is to the right, trigger right swipe action (restores homepage)
      else if (touchstartX < touchendX && !isSwiping) {
        swipeDirection = 'right';
        isSwiping = true;
        lockPageRendering(); // Lock page during swipe
        console.log("Mouse right swipe detected");

        handleSwipe(); // Perform the right swipe action
      }
    }
  }

  function handleMouseUp() {
    // Reset after mouse swipe
    if (isSwiping) {
      isSwiping = false;
      console.log("Mouse swipe transition complete");
    }
  }

  document.addEventListener('mousemove', handleMouseMove, { passive: false });
  document.addEventListener('mouseup', handleMouseUp);
}

// For mouse events (desktop swipe)
document.addEventListener('mousedown', detectMouseSwipe);
