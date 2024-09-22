function q2_contar_frequenciaa_palavra(text) {
    let num_rep_hello = 0;
    let num_rep_word = 0;

    const words = text.split(" ");
    for (const name of words) {
        if (name === "Hello" || name === "hello") {
            num_rep_hello++;
        }
        if (name === "World" || name === "world") {
            num_rep_word++;
        }
    }
    console.log(`Hello: ${num_rep_hello} World: ${num_rep_word}`);
}

const text = 'Hello world hello';
q2_contar_frequenciaa_palavra(text);
