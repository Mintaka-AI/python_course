"use strict";

const MODULE_ORDER = [
  "00_environment",
  "01_python_basics",
  "02_engineering_code",
  "03_math_and_data",
  "04_engineering_calculations",
  "05_ai_and_llm",
  "06_engineering_ai_agents",
];

const STATUS_LABELS = {
  not_started: "Not started",
  in_progress: "In progress",
  completed: "Completed",
};

async function loadCourseState(statePath = "state.json") {
  const response = await fetch(statePath);

  if (!response.ok) {
    throw new Error(`Failed to load ${statePath}: ${response.status}`);
  }

  return response.json();
}

function buildCourseSummary(state) {
  const modules = MODULE_ORDER.map((id) => ({
    id,
    ...state.modules[id],
  }));

  const completedModules = modules.filter((module) => module.status === "completed");
  const inProgressModules = modules.filter((module) => module.status === "in_progress");
  const totalBlocks = modules.length * 3;
  const masteredBlocks = modules.reduce((count, module) => {
    return (
      count +
      Number(module.theory.mastered) +
      Number(module.examples.mastered) +
      Number(module.code.mastered)
    );
  }, 0);

  const currentModule = state.modules[state.course.current_module];

  return {
    student: state.course.student || "Not set",
    currentModuleId: state.course.current_module,
    currentModuleTitle: currentModule ? currentModule.title : "Unknown",
    startedAt: state.course.started_at,
    lastSession: state.course.last_session,
    totalModules: modules.length,
    completedModules: completedModules.length,
    inProgressModules: inProgressModules.length,
    overallPercent: Math.round((masteredBlocks / totalBlocks) * 100),
    masteredBlocks,
    totalBlocks,
    modules,
  };
}

function formatDate(value) {
  if (!value) {
    return "—";
  }

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return value;
  }

  return date.toLocaleString();
}

function renderBlockStatus(label, block) {
  const statusClass = block.mastered ? "status-pass" : "status-pending";
  const statusText = block.mastered ? "Mastered" : "Pending";
  const details = [];

  if (label === "Theory" && block.score !== null) {
    details.push(`Score: ${block.score}%`);
  }

  if (block.attempts > 0) {
    details.push(`Attempts: ${block.attempts}`);
  }

  if (block.completed && block.completed.length > 0) {
    details.push(`Completed: ${block.completed.join(", ")}`);
  }

  return `
    <div class="block-status">
      <span class="block-label">${label}</span>
      <span class="status-badge ${statusClass}">${statusText}</span>
      ${details.length > 0 ? `<span class="block-details">${details.join(" · ")}</span>` : ""}
    </div>
  `;
}

function renderModuleCard(module, currentModuleId) {
  const isCurrent = module.id === currentModuleId;
  const cardClass = [
    "module-card",
    `module-${module.status}`,
    isCurrent ? "module-current" : "",
  ]
    .filter(Boolean)
    .join(" ");

  return `
    <article class="${cardClass}">
      <header class="module-header">
        <h3>${module.title}</h3>
        <span class="status-badge status-${module.status}">${STATUS_LABELS[module.status] || module.status}</span>
      </header>
      <p class="module-id"><code>${module.id}</code></p>
      ${renderBlockStatus("Theory", module.theory)}
      ${renderBlockStatus("Examples", module.examples)}
      ${renderBlockStatus("Code", module.code)}
    </article>
  `;
}

function renderCourseSummary(container, summary) {
  container.innerHTML = `
    <section class="summary-cards">
      <div class="summary-card">
        <span class="summary-label">Student</span>
        <strong>${summary.student}</strong>
      </div>
      <div class="summary-card">
        <span class="summary-label">Current module</span>
        <strong>${summary.currentModuleTitle}</strong>
      </div>
      <div class="summary-card">
        <span class="summary-label">Modules completed</span>
        <strong>${summary.completedModules} / ${summary.totalModules}</strong>
      </div>
      <div class="summary-card">
        <span class="summary-label">Overall progress</span>
        <strong>${summary.overallPercent}%</strong>
        <span class="summary-meta">${summary.masteredBlocks} / ${summary.totalBlocks} blocks</span>
      </div>
    </section>

    <section class="summary-meta-row">
      <p><strong>Started:</strong> ${formatDate(summary.startedAt)}</p>
      <p><strong>Last session:</strong> ${formatDate(summary.lastSession)}</p>
      <p><strong>In progress:</strong> ${summary.inProgressModules}</p>
    </section>

    <div class="progress-bar" role="progressbar" aria-valuenow="${summary.overallPercent}" aria-valuemin="0" aria-valuemax="100">
      <div class="progress-fill" style="width: ${summary.overallPercent}%"></div>
    </div>

    <section class="module-list">
      <h2>Modules</h2>
      <div class="module-grid">
        ${summary.modules.map((module) => renderModuleCard(module, summary.currentModuleId)).join("")}
      </div>
    </section>
  `;
}

async function initCourseSummary(containerSelector, statePath = "state.json") {
  const container =
    typeof containerSelector === "string"
      ? document.querySelector(containerSelector)
      : containerSelector;

  if (!container) {
    return;
  }

  try {
    const state = await loadCourseState(statePath);
    const summary = buildCourseSummary(state);
    renderCourseSummary(container, summary);
  } catch (error) {
    container.innerHTML = `
      <div class="warning">
        <p><strong>Could not load course progress.</strong></p>
        <p>${error.message}</p>
        <p>Open this page through a local web server so <code>state.json</code> can be loaded.</p>
      </div>
    `;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-copy-code]").forEach((button) => {
    button.addEventListener("click", async () => {
      const selector = button.dataset.copyCode;
      const codeBlock = selector ? document.querySelector(selector) : null;

      if (!codeBlock) {
        return;
      }

      await navigator.clipboard.writeText(codeBlock.textContent);
      const originalText = button.textContent;
      button.textContent = "Copied";

      window.setTimeout(() => {
        button.textContent = originalText;
      }, 1500);
    });
  });
});
