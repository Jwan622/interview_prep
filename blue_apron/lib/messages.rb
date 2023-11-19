class Messages
  def self.introduction(strategy_name)
    "===================================================================\n" +
    "              __       __   __            __     _____   __     \n" +
    "\\    /\\    / |    |   |    |  | |\\    /| |         |    |  |    \n" +
    " \\  /  \\  /  |--  |   |    |  | | \\  / | |--       |    |  |    \n" +
    "  \\/    \\/   |__  |__ |__  |__| |  \\/  | |__       |    |__|    \n" +
    "                    ___    ___     ____                           \n" +
    "                    |  )  |   |   |                               \n" +
    "                    |_)   |___|   |                               \n" +
    "                    |\\    |       |____                           \n" +
    "                    | \\   |            |                          \n" +
    "                    |  \\  |       _____|                          \n" +
    "===================================================================\n" +
    "You are playing against strategy #{strategy_name}."
  end

  def self.display_options
    "Type 'r', 'p' or 's'. Or type 'q' to quit."
  end

  def self.invalid_input
    "Your input is invalid."
  end

  def self.computer_play_and_eval(comp_decision, victor)
    "I chose #{comp_decision}. " + victor
  end

  def self.end_game
    "Thanks for playing. Goodbye!"
  end

  def self.announce_score(user_score, computer_score, tie_score)
    "You won #{user_score} times.\nYou lost #{computer_score} times.\nWe tied #{tie_score} times.\n"
  end

  def self.invalid_strategy
    "The strategy you passed in was invalid so a random strategy was selected for you. Good luck!"
  end

  def self.invalid_input_stream
    "The input stream you passed in was invalid so you will have to provide your own choices via the keyboard."
  end

  def self.invalid_output_stream
    "The output stream you passed in was invalid so the output will be displayed on your terminal."
  end
end
