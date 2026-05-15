async function translateQuery() {

    const query = document.getElementById("queryInput").value;

    if(query.trim() === ""){
        alert("Please enter a query");
        return;
    }

    const response = await fetch("/translate", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            query: query
        })
    });

    const data = await response.json();

    document.getElementById("language").innerText =
        data.detected_language;

    document.getElementById("translated").innerText =
        data.translated_text;

    document.getElementById("response").innerText =
        data.support_response;
}