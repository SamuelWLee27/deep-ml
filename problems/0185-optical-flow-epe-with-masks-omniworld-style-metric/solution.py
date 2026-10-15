from typing import Optional, Union

try:
    import numpy as np
except Exception:
    np = None

ArrayLike = Union[list, "np.ndarray"]

def flow_epe(pred: ArrayLike,
             gt: ArrayLike,
             mask: Optional[ArrayLike] = None,
             max_flow: Optional[float] = None) -> float:
    """
    Compute mean End-Point Error (EPE) between predicted and ground-truth optical flow.

    Args:
        pred, gt: (H, W, 2) lists or NumPy arrays.
        mask: optional (H, W) or broadcastable to (H, W); 1=include, 0=ignore.
        max_flow: optional float; clip per-pixel EPE to this value.

    Returns:
        float: mean EPE over valid pixels. Returns -1 on invalid input or if no valid pixels.
    """
    epe_sum = 0
    epe_count = 0
    try:
        if len(pred) != len(gt):
                return -1.0

        for i in range(len(pred)):

            if len(pred[i]) != len(gt[i]):
                    return -1.0

            for j in range(len(pred[i])):

                pred_flow = pred[i][j]
                gt_flow = gt[i][j]

                if len(pred_flow) != 2 or len(gt_flow) != 2:
                    return -1.0

                
                if mask and not mask[i][j]:
                    continue
                
                dx = float(pred_flow[0]) - float(gt_flow[0])
                dy = float(pred_flow[1]) - float(gt_flow[1])
                epe = np.sqrt(dx * dx + dy * dy)

                if epe != epe or epe == float("inf"):
                    continue 

                if max_flow:
                    epe = min(epe, max_flow)

                epe_sum += epe
                epe_count += 1
    except (TypeError, ValueError, IndexError):
        return -1.0

    if epe_sum == 0:
        return 0

    epe_mean = epe_sum / epe_count

    return epe_mean


    
