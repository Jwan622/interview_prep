require 'spec_helper'

describe ARGVChecker do
  let(:valid_strategies) { ["favorite", "last", "champ"] }
  let (:valid_input_streams) { [$stdin] }
  let (:valid_output_streams) { [$stdout] }

  it "correctly returns valid strategies if none are provided" do
    fake_argv = []

    cleaned_argv = ARGVChecker.process(fake_argv)

    expect(valid_strategies).to include(cleaned_argv[0])
  end

  it "correctly returns valid strategies if an invalid one is provided" do
    fake_argv = ["invalid strategy", $stdin, $stdout]

    cleaned_argv = ARGVChecker.process(fake_argv)

    expect(valid_strategies).to include(cleaned_argv[0])
  end

  it "correctly returns a valid input_stream if none are provided" do
    fake_argv = ["favorite"]

    cleaned_argv = ARGVChecker.process(fake_argv)

    expect(valid_input_streams).to include(cleaned_argv[1])
  end

  it "correctly returns a valid input_stream if an invalid one is provided" do
    fake_argv = ["favorite", "invalid input stream"]

    cleaned_argv = ARGVChecker.process(fake_argv)

    expect(valid_input_streams).to include(cleaned_argv[1])
  end

  it "correctly returns a valid output_stream if none are provided" do
    fake_argv = ["favorite", $stdin]

    cleaned_argv = ARGVChecker.process(fake_argv)

    expect(valid_output_streams).to include(cleaned_argv[2])
  end

  it "correctly returns a valid output_stream if an invalid one is provided" do
    fake_argv = ["favorite", $stdin, "invalid output stream"]

    cleaned_argv = ARGVChecker.process(fake_argv)

    expect(valid_output_streams).to include(cleaned_argv[2])
  end

  it "correctly returns a valid strategy, input_stream, and output_stream if none are provided" do
    fake_argv = []
    valid_possibilities = [["favorite", $stdin, $stdout], ["last", $stdin, $stdout],["champ", $stdin, $stdout]]

    cleaned_argv = ARGVChecker.process(fake_argv)

    expect(valid_possibilities).to include(cleaned_argv)
  end

  it "correctly returns a valid strategy, input_stream, and output_stream if invalid ones are provided" do
    fake_argv = ["invalid strat", "invalid input_stream", "invalid output stream"]
    valid_possibilities = [["favorite", $stdin, $stdout], ["last", $stdin, $stdout],["champ", $stdin, $stdout]]

    cleaned_argv = ARGVChecker.process(fake_argv)

    expect(valid_possibilities).to include(cleaned_argv)
  end
end
