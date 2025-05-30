module.exports = {
  content: [
    "./shop1django/templates/**/*.html",
    "./shop1django/static/**/*.js",
  ],
    variants: {
      extend: {
          scale: ['group-hover'],
          transform: ['group-hover'],
          opacity: ['group-hover']
      }
  },
  theme: {
    extend: {},
  },
  plugins: [],
  
}