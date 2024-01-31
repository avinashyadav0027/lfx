let predefined_responses = [
  ("hello", "Hi there!");
  ("how are you", "I'm just a program, but thanks for asking!");
  ("what's your name", "I'm a chatbot, so I don't have a name!");
  ("who created you", "I was created by a programmer using OCaml.");
  ("how does it work", "I use pattern matching to match user input with predefined responses.");
  ("tell me a joke", "Why don't scientists trust atoms? Because they make up everything!");
  ("favorite color", "I don't have a favorite color. What's yours?");
  ("thanks", "You're welcome!");
  ("what can you do", "I can just respond to some predefined prompts");
  ("bye", "Goodbye! Have a great day.");
]

let rec get_response user_input =
  match List.assoc_opt (String.lowercase_ascii user_input) predefined_responses with
  | Some(response) -> response
  | None ->
      print_endline "I didn't understand. Can you rephrase?";
      let new_input = read_line () in
      get_response new_input

let () =
  print_endline "Hello! I'm a simple chatbot.";
  print_endline "You can start chatting with me. Type 'bye' to exit.";

  let rec chat_loop () =
    print_string "> ";
    flush stdout;
    let user_input = read_line () in

    if String.lowercase_ascii user_input = "bye" then
      print_endline "Goodbye! Have a great day."
    else begin
      let response = get_response user_input in
      print_endline response;
      chat_loop ()
    end
  in

  chat_loop ()
