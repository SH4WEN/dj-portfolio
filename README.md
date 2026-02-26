# DJ Portfolio

A Django-based portfolio website featuring neumorphic design and interactive elements.

## Features

- **Neumorphic UI Design**: Soft, extruded plastic design style with subtle shadows
- **Dark/Light Theme Toggle**: Automatic theme detection with manual override
- **Interactive Flip Animation**: Profile and project images with flip functionality
- **Responsive Layout**: Works on mobile, tablet, and desktop devices
- **Loading Animations**: Custom loading screen with spinner

## Flip Animation Feature

The portfolio includes a flip animation feature that enhances user interaction:

### Profile Image Flip

- Click on the profile image to flip it and reveal a "sleep" image
- In dark mode, the sleep image is shown by default
- In light mode, the normal profile image is shown by default
- The flip animation has a smooth 0.6 second transition

### Project Image Flip

- Project images also support the flip animation
- Similar behavior to profile images with theme-aware defaults
- Enhances the user experience when browsing projects

### Technical Implementation

- Uses CSS 3D transforms for the flip effect
- JavaScript handles the click events and theme synchronization
- The `.flip-container` class enables the flip functionality
- The `.flipped` class triggers the 180-degree rotation
- Theme awareness ensures appropriate images show based on current theme

## Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## Technologies Used

- Django (Python web framework)
- Tailwind CSS (via CDN)
- Lucide Icons
- Custom JavaScript for animations and interactions
- Neumorphic design principles

## Customization

To customize the flip animation:

1. Modify the CSS in `base.html` within the `<style>` tags
2. Update the JavaScript functions `toggleFlip()` and `updateFlipDisplay()` in `base.html`
3. Adjust the timing in the CSS transition property for faster/slower animations
