async function updateMessages() {
  try {
    const res = await fetch('/api/latest_messages');
    const msgs = await res.json();
    const table = document.getElementById("messageTable").getElementsByTagName('tbody')[0];
    table.innerHTML = "";
    let botCount = 0;
    msgs.forEach(m => {
      const row = table.insertRow();
      const isBot = m.bot_suspect === true;
      if (isBot) botCount++;
      row.innerHTML = `<td>${m.user_id}</td><td>${m.text}</td><td>${m.analysis?.category || "?"}</td><td style="color:${isBot ? 'red' : 'green'};">${isBot ? '🤖' : '✅'}</td>`;
    });
    updateRiskLevel(botCount / msgs.length);
  } catch (error) {
    console.error('Error fetching messages:', error);
  }
}

async function updateAlerts() {
  try {
    const res = await fetch('/api/alerts');
    const alerts = await res.json();
    const table = document.getElementById("alertTable").getElementsByTagName('tbody')[0];
    table.innerHTML = "";
    alerts.forEach(alert => {
      const row = table.insertRow();
      row.innerHTML = `<td>${alert.type}</td><td>${alert.message}</td><td>${alert.level}</td><td>${new Date(alert.timestamp).toLocaleString()}</td>`;
    });
  } catch (error) {
    console.error('Error fetching alerts:', error);
  }
}

function updateRiskLevel(botRatio) {
  const el = document.getElementById("riskLevel");
  if (botRatio > 0.3) {
    el.innerText = "Høy"; el.style.color = "red";
  } else if (botRatio > 0.1) {
    el.innerText = "Medium"; el.style.color = "orange";
  } else {
    el.innerText = "Lav"; el.style.color = "green";
  }
}

// Initial load
updateMessages();
updateAlerts();

// Auto-refresh every 5 seconds
setInterval(() => {
  updateMessages();
  updateAlerts();
}, 5000);
