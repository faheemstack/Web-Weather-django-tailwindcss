/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Django templates
    "./static/**/*.js", //JS files in static
    "./static/**/*.ts",
    "./static/**/*.jsx",
    "./static/**/*.tsx",
  ],
  theme: {
    extend: {
      extend: {
        colors: {
          navy: "#0c1a2e",
          accent: "#ffd166",
        },
        fontFamily: {
          syne: ["Syne", "sans-serif"],
          dm: ["DM Sans", "sans-serif"],
        },
        keyframes: {
          slideDown: {
            from: { opacity: "0", transform: "translateY(-30px)" },
            to: { opacity: "1", transform: "translateY(0)" },
          },
          fadeUp: {
            from: { opacity: "0", transform: "translateY(10px)" },
            to: { opacity: "1", transform: "translateY(0)" },
          },
          drift: {
            "0%": { transform: "translate(0,0) scale(1)" },
            "100%": { transform: "translate(40px,30px) scale(1.08)" },
          },
          float: {
            "0%,100%": { transform: "translateY(0)" },
            "50%": { transform: "translateY(-14px)" },
          },
          twinkle: { "0%": { opacity: "0.2" }, "100%": { opacity: "1" } },
        },
        animation: {
          slideDown: "slideDown 0.7s ease both",
          fadeUp: "fadeUp 0.5s ease both",
          drift1: "drift 20s ease-in-out infinite alternate",
          drift2: "drift 15s ease-in-out infinite alternate",
          drift3: "drift 25s ease-in-out infinite alternate",
          float: "float 4s ease-in-out infinite",
          twinkle: "twinkle 3s ease-in-out infinite alternate",
        },
      },
    },
  },
  plugins: [],
};
