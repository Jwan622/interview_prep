class ARGVChecker
  VALID_STRAT = ["favorite", "last", "champ"]
  VALID_INPUT = [$stdin]
  VALID_OUTPUT = [$stdout]

  attr_reader :strategy,
              :input_stream,
              :output_stream

  def self.process(uncleaned_argv)
    uncleaned_strategy, uncleaned_input_stream, uncleaned_output_stream = uncleaned_argv[0], uncleaned_argv[1], uncleaned_argv[2]
    strategy = process_strategy(uncleaned_strategy)
    input_stream = process_input_stream(uncleaned_input_stream)
    output_stream = process_output_stream(uncleaned_output_stream)
    [strategy, input_stream, output_stream]
  end

  private

  def self.process_strategy(strategy)
    if detects_invalid_strategy?(strategy) || strategy.nil?
      @strategy = random_valid_strategy
    else
      @strategy = strategy
    end
  end

  def self.process_input_stream(input_stream)
    if detects_invalid_input_stream?(input_stream)
      @input_stream = $stdin
    else
      @input_stream = input_stream
    end
  end

  def self.process_output_stream(output_stream)
    if detects_invalid_output_stream?(output_stream)
      @output_stream = $stdout
    else
      @output_stream = output_stream
    end
  end

  def self.detects_invalid_strategy?(strategy)
    !VALID_STRAT.include?(strategy)
  end

  def self.detects_invalid_input_stream?(input_stream)
    !VALID_INPUT.include?(input_stream)
  end

  def self.detects_invalid_output_stream?(output_stream)
    !VALID_OUTPUT.include?(output_stream)
  end

  def self.random_valid_strategy
    VALID_STRAT.sample
  end
end
