def generate_conversation(summary, key_points):
    """
    Generate a conversational script between two hosts.
    
    :param summary: Summary of the paper.
    :param key_points: List of key points from the paper.
    :return: List of lines for the conversation script.
    """
    script = [
        "Host 1: Hey everyone, welcome to PaperPod! Today we're diving into an exciting research paper.",
        f"Host 2: That's right! Here's a quick summary: {summary}",
        "Host 1: Interesting! What are some key takeaways from this paper?"
    ]
    
    for i, point in enumerate(key_points, 1):
        script.append(f"Host 2: Key point {i}: {point}")
        script.append(f"Host 1: Wow, that's fascinating! Can you elaborate on how this impacts the field?")
        script.append(f"Host 2: Well, it suggests that {point.split('.')[0]} could lead to new research directions.")

    script.append("Host 1: That's all for today. Thanks for tuning in!")
    script.append("Host 2: See you next time on PaperPod!")
    
    return script