// tailwind.config.js
module.exports = {
  content: [
    './templates/**/*.html', // Ensure your templates are included here
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),  // This is the forms plugin
  ],
}
