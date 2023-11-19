require 'spec_helper'

describe Printer do
  attr_reader :printer

  before :each do
    @printer = Printer.new(STDOUT)
  end

  it "should output the message to console" do
    expect { printer.print("hello world") }.
      to output("hello world\n").to_stdout_from_any_process
  end
end
