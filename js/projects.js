async function initProjectLinks() {
  const frame = document.querySelector(".page-frame[data-projects]");
  if (!frame) return;

  const response = await fetch("data/projects.json");
  const projects = await response.json();

  for (const project of projects) {
    const link = document.createElement("a");
    link.className = "project-link";
    link.style.left = `${project.x}%`;
    link.style.top = `${project.y}%`;
    link.style.width = `${project.width}%`;
    link.style.height = `${project.height}%`;
    link.setAttribute("aria-label", project.label);
    link.title = project.label;

    if (project.href) {
      link.href = project.href;
      if (project.href.startsWith("http")) {
        link.target = "_blank";
        link.rel = "noopener noreferrer";
      }
    } else {
      link.classList.add("disabled");
      link.href = "#";
      link.addEventListener("click", (event) => event.preventDefault());
    }

    frame.appendChild(link);
  }
}

initProjectLinks();
