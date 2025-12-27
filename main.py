import torch


def main():
    my_tensor = torch.tensor(
        data=[
            [[0, 6, 3], [24, 1, 1], [22, 44, 11], [0, 0, 1]],
            [[49, 1, 2], [48, 2, 5], [99, 1, -1], [0, 1, 2]],
        ]
    )
    print(my_tensor, my_tensor.shape)
    print(my_tensor[0][-1])
    print(my_tensor[1])
    print(my_tensor[0][1:3])
    print(my_tensor[:, 0, :], my_tensor[:, 0, :].shape)
    print(my_tensor[:, -2:, :])


if __name__ == "__main__":
    main()
